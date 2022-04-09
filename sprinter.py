# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sprinter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 651, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.minutes_per_sprint_label = QtWidgets.QLabel(self.layoutWidget)
        self.minutes_per_sprint_label.setWordWrap(True)
        self.minutes_per_sprint_label.setObjectName("minutes_per_sprint_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minutes_per_sprint_label)
        self.minutes_per_sprint_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.minutes_per_sprint_spinbox.setObjectName("minutes_per_sprint_spinbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minutes_per_sprint_spinbox)
        self.target_wordcount_label = QtWidgets.QLabel(self.layoutWidget)
        self.target_wordcount_label.setWordWrap(True)
        self.target_wordcount_label.setObjectName("target_wordcount_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.target_wordcount_label)
        self.target_wordcount_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.target_wordcount_spinbox.setObjectName("target_wordcount_spinbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.target_wordcount_spinbox)
        self.severity_label = QtWidgets.QLabel(self.layoutWidget)
        self.severity_label.setObjectName("severity_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.severity_label)
        self.severity_slider = QtWidgets.QSlider(self.layoutWidget)
        self.severity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.severity_slider.setObjectName("severity_slider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.severity_slider)
        self.horizontalLayout.addLayout(self.formLayout)
        self.start_button = QtWidgets.QPushButton(self.layoutWidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textarea = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.textarea.setObjectName("textarea")
        self.verticalLayout.addWidget(self.textarea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wordcount_label = QtWidgets.QLabel(self.layoutWidget)
        self.wordcount_label.setObjectName("wordcount_label")
        self.horizontalLayout_2.addWidget(self.wordcount_label)
        self.wordcount_value_label = QtWidgets.QLabel(self.layoutWidget)
        self.wordcount_value_label.setObjectName("wordcount_value_label")
        self.horizontalLayout_2.addWidget(self.wordcount_value_label)
        self.wordcount_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.wordcount_progressBar.setProperty("value", 0)
        self.wordcount_progressBar.setObjectName("wordcount_progressBar")
        self.horizontalLayout_2.addWidget(self.wordcount_progressBar)
        self.time_remaining_label = QtWidgets.QLabel(self.layoutWidget)
        self.time_remaining_label.setObjectName("time_remaining_label")
        self.horizontalLayout_2.addWidget(self.time_remaining_label)
        self.time_remaining_value_label = QtWidgets.QLabel(self.layoutWidget)
        self.time_remaining_value_label.setObjectName("time_remaining_value_label")
        self.horizontalLayout_2.addWidget(self.time_remaining_value_label)
        self.time_remaining_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.time_remaining_progressBar.setProperty("value", 100)
        self.time_remaining_progressBar.setObjectName("time_remaining_progressBar")
        self.horizontalLayout_2.addWidget(self.time_remaining_progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minutes_per_sprint_label.setText(_translate("MainWindow", "Minutes per sprint"))
        self.target_wordcount_label.setText(_translate("MainWindow", "Target wordcount"))
        self.severity_label.setText(_translate("MainWindow", "Severity"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.textarea.setPlainText(_translate("MainWindow", "Write here..."))
        self.wordcount_label.setText(_translate("MainWindow", "Word count"))
        self.wordcount_value_label.setText(_translate("MainWindow", "0"))
        self.time_remaining_label.setText(_translate("MainWindow", "Time remaining"))
        self.time_remaining_value_label.setText(_translate("MainWindow", "0"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

