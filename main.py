import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex

from sprinter import Ui_MainWindow
from session import Session
from text import Text
from utils import make_darktheme_palette, make_alarm_palette


class Worker(QObject):
    """Class for process running in background thread"""

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self):
        QObject.__init__(self)
        self._mutex = QMutex()
        self._running = True

    #@pyqtSlot()
    def stop(self):
        """
        Switches infinite while loop condition to False
        """
#       self._mutex.lock()
        self._running = False
#        self._mutex.unlock()

    def running(self):
        #try:
        #    self._mutex.lock()
            return self._running
        #finally:
        #    self._mutex.unlock()

    #@pyqtSlot()
    def run_session(self):

        while self.running():
            time.sleep(5)
            self.progress.emit(1)
        self.finished.emit()


class SprinterMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app, parent=None):

        super(SprinterMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.app = app

        # Force the style to be the same on all OSs:
        self.app.setStyle("Fusion")

        palette = make_darktheme_palette()
        self.app.setPalette(palette)

        self.start_button.clicked.connect(self.start_session_in_thread)
        self.textarea.textChanged.connect(self.update_textchanged_time)
        self.textarea.installEventFilter(self)

        self.session = None

    # def eventFilter(self, source, event):
    #     if event.type() == QtCore.QEvent.FocusIn and source is self.ledit_corteA:
    #         print("A")
    #         self.flag = 0
    #     if event.type() == QtCore.QEvent.FocusIn and source is self.ledit_corteB:
    #         print("B")
    #         self.flag = 1
    #     return super(MainWindow, self).eventFilter(source, event)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.textarea:
            if event.key() == QtCore.Qt.Key_Return and self.textarea.hasFocus():
                print('Enter pressed')
        return super().eventFilter(obj, event)
        

    def start_session_in_thread(self):

        minutes_per_sprint = self.minutes_per_sprint_spinbox.value()
        target_wordcount = self.target_wordcount_spinbox.value()
        severity = self.severity_slider.value()

        initial_text_string = self.textarea.toPlainText()

        text = Text(initial_text_string=initial_text_string)
        self.session = Session(minutes_per_sprint=minutes_per_sprint,
                               target_wordcount=target_wordcount,
                               severity=severity,
                               text=text)

        print('starting session')
        self.thread = QThread()
        self.worker = Worker()

        # move worker to the thread
        self.worker.moveToThread(self.thread)

        # connect signals and slots
        self.thread.started.connect(self.worker.run_session)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_status)

        self.update_status()

        self.thread.start()

        # Final resets
        self.start_button.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.start_button.setEnabled(True)
        )
        #self.thread.finished.connect(
        #    lambda: self.wordcount_value_label.setText("Long-Running Step: 0")
        #)

    def update_status(self):

        print('update_status')

        if (self.session.seconds_remaining > 0) and (self.session.words_remaining > 0):

            current_text_string = self.textarea.toPlainText()

            # update all session variables
            self.session.update_session_status(current_text_string)

            # update text in labels in UI
            self.update_status_bar()

            self.check_alarm_condition()

            return

        if self.session.seconds_remaining <=0:
            self.worker.stop()
            print('Times up!')

        if self.session.words_remaining <= 0:
            self.worker.stop()
            print('Well done!')

    def update_status_bar(self):
        """
        Update text in labels in the status bar in the UI.
        """

        added_wordcount = self.session.text.added_wordcount
        minutes_remaining = self.session.minutes_remaining
        perc_time_remaining = self.session.perc_time_remaining
        perc_wc_achieved = self.session.perc_wc_achieved

        tr_text = f'{minutes_remaining}:00'
        self.time_remaining_value_label.setText(tr_text)
        self.time_remaining_progressBar.setProperty("value", perc_time_remaining)
        wc_text = f'{added_wordcount} / {self.session.target_wordcount}'
        self.wordcount_value_label.setText(wc_text)
        self.wordcount_progressBar.setProperty("value", perc_wc_achieved)
    
    def check_alarm_condition(self):
        """
        Change app colour scheme based on number of seconds since last
        user interaction with text area

        # TODO linear change from pink to red
        """

        seconds_since_last_interaction = time.time() - self.session.time_lastmodified_textarea

        if seconds_since_last_interaction > self.session.seconds_allowed_since_lastmodified:
            palette = make_alarm_palette()
        else:
            palette = make_darktheme_palette()

        self.app.setPalette(palette)

    def update_textchanged_time(self):
        """
        Record the time at which the user last changed the text
        in the textarea
        """

        if self.session:
            self.session.time_lastmodified_textarea = time.time()

    def backup_text_to_disk(self):
        """
        Save contents of textarea to temporary file on disk
        """

        current_text_string = self.textarea.toPlainText()

        with open('sprinter.bkp.txt', 'w') as f:
            f.write(current_text_string)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = SprinterMainWindow(app)
    window.show()
    
    sys.exit(app.exec_())