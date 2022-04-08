import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from sprinter import Ui_MainWindow


def test():
    print('yay!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.start_button.clicked.connect(test)
    MainWindow.show()
    sys.exit(app.exec_())
