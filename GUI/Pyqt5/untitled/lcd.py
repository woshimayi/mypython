# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(20, 20, 101, 61))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu23 = QtWidgets.QMenu(self.menuBar)
        self.menu23.setObjectName("menu23")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menu23.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu23.setTitle(_translate("MainWindow", "23"))

if __name__ == '__main__':
	app = QApplication(sys.argv)

	MainWindow = QtWidgets.QMainWindow()

	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.retranslateUi(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())

