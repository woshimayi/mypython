# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\zsfile\python27\GUI\Pyqt5\xbox\xbox_display.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setGeometry(QtCore.QRect(121, 250, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_2.setGeometry(QtCore.QRect(61, 290, 51, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_3.setGeometry(QtCore.QRect(191, 290, 51, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_4.setGeometry(QtCore.QRect(121, 330, 61, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_5.setGeometry(QtCore.QRect(500, 390, 61, 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_6.setGeometry(QtCore.QRect(420, 420, 71, 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_7.setGeometry(QtCore.QRect(570, 420, 61, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_8.setGeometry(QtCore.QRect(500, 440, 61, 22))
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_9.setGeometry(QtCore.QRect(130, 50, 42, 22))
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_10.setGeometry(QtCore.QRect(590, 40, 42, 22))
        self.spinBox_10.setObjectName("spinBox_10")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 440, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 460, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 460, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 480, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 130, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 130, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 80, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 290, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_11.setGeometry(QtCore.QRect(480, 310, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 310, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_13.setGeometry(QtCore.QRect(550, 330, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LT"))
        self.pushButton_2.setText(_translate("MainWindow", "RT"))
        self.pushButton_3.setText(_translate("MainWindow", "UP"))
        self.pushButton_4.setText(_translate("MainWindow", "LEFT"))
        self.pushButton_5.setText(_translate("MainWindow", "RIGHT"))
        self.pushButton_6.setText(_translate("MainWindow", "DOWN"))
        self.pushButton_7.setText(_translate("MainWindow", "start"))
        self.pushButton_8.setText(_translate("MainWindow", "back"))
        self.pushButton_9.setText(_translate("MainWindow", "xbox"))
        self.pushButton_10.setText(_translate("MainWindow", "Y"))
        self.pushButton_11.setText(_translate("MainWindow", "X"))
        self.pushButton_12.setText(_translate("MainWindow", "B"))
        self.pushButton_13.setText(_translate("MainWindow", "A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())