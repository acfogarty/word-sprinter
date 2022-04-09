import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex

from sprinter import Ui_MainWindow
from session import Session
from text import Text
from utils import make_darktheme_palette


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
        self._mutex.lock()
        self._running = False
        self._mutex.unlock()

    def running(self):
        try:
            self._mutex.lock()
            return self._running
        finally:
            self._mutex.unlock()

    #@pyqtSlot()
    def run_session(self):

        while self.running():
            time.sleep(1)
            self.progress.emit(1)
        self.finished.emit()


class Main:

    def __init__(self):

        self.ui = None
        self.session = None

    def launch(self, MainWindow):
        """
        Setup UI, slots and signals on first launch
        """

        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.start_button.clicked.connect(self.start_session_in_thread)

    def start_session_in_thread(self):

        minutes_per_sprint = self.ui.minutes_per_sprint_spinbox.value()
        target_wordcount = self.ui.target_wordcount_spinbox.value()
        severity = self.ui.severity_slider.value()

        initial_text_string = self.ui.textarea.toPlainText()

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

        self.thread.start()

        # Final resets
        self.ui.start_button.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.ui.start_button.setEnabled(True)
        )
        #self.thread.finished.connect(
        #    lambda: self.ui.wordcount_value_label.setText("Long-Running Step: 0")
        #)

    def update_status(self):

        if (self.session.seconds_remaining > 0) and (self.session.words_remaining > 0):
            current_text_string = self.ui.textarea.toPlainText()

            # update all session variables
            self.session.update_session_status(current_text_string)

            # update text in labels in UI
            self.update_status_bar()

            return

        if self.session.seconds_remaining <=0:
            print('Times up!')
            self.worker.stop()

        if self.session.words_remaining <= 0:
            print('Well done!')
            self.worker.stop()

    def update_status_bar(self):
        """
        Update text in labels in the status bar in the UI.
        """

        added_wordcount = self.session.text.added_wordcount
        minutes_remaining = self.session.minutes_remaining
        perc_time_remaining = self.session.perc_time_remaining
        perc_wc_achieved = self.session.perc_wc_achieved

        tr_text = f'{minutes_remaining}:00'
        self.ui.time_remaining_value_label.setText(tr_text)
        self.ui.time_remaining_progressBar.setProperty("value", perc_time_remaining)
        wc_text = f'{added_wordcount} / {self.session.target_wordcount}'
        self.ui.wordcount_value_label.setText(wc_text)
        self.ui.wordcount_progressBar.setProperty("value", perc_wc_achieved)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")
    palette = make_darktheme_palette()
    app.setPalette(palette)

    MainWindow = QtWidgets.QMainWindow()
    main = Main()
    main.launch(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())