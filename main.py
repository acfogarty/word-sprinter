import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from sprinter import Ui_MainWindow
from session import Session


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

        nminutes_per_sprint = self.ui.minutes_per_sprint_spinbox.value()

        self.text = Text(initial_text_string=initial_text_string)
        self.session = Session(nminutes_per_sprint=nminutes_per_sprint)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    main = Main()
    main.launch(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())



