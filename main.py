import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from sprinter import Ui_MainWindow
from session import Session
from text import Text
from utils import make_darktheme_palette


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
        self.ui.start_button.clicked.connect(self.start_session)

    def start_session(self):

        minutes_per_sprint = self.ui.minutes_per_sprint_spinbox.value()
        target_wordcount = self.ui.target_wordcount_spinbox.value()
        severity = self.ui.severity_slider.value()

        initial_text_string = self.ui.textarea.toPlainText()

        text = Text(initial_text_string=initial_text_string)
        self.session = Session(minutes_per_sprint=minutes_per_sprint,
                               target_wordcount=target_wordcount,
                               severity=severity,
                               text=text)

        self.update_status(current_text_string=initial_text_string)

    def update_status(self, current_text_string: str):

        current_total_wordcount, current_delta_wordcount = self.session.text.get_wordcount_info(current_text_string)
        minutes_remaining = 7

        self.ui.time_remaining_value_label.setText(f'{minutes_remaining}:00')
        self.ui.wordcount_value_label.setText(f'{current_delta_wordcount} / {self.session.target_wordcount}')

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



