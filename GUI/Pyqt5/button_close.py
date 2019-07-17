# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button_close.ui'
#
<<<<<<< HEAD
# Created by: PyQt5 UI code generator 5.6
=======
# Created by: PyQt5 UI code generator 5.11.2
>>>>>>> d98fb1c44e2d640a5fecdc100702606f65a4875f
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
<<<<<<< HEAD


=======
>>>>>>> d98fb1c44e2d640a5fecdc100702606f65a4875f
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
<<<<<<< HEAD
        self.pushButton.setGeometry(QtCore.QRect(60, 40, 91, 101))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 170, 200, 110))
        self.calendarWidget.setObjectName("calendarWidget")
=======
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 91, 101))
        self.pushButton.setObjectName("pushButton")
>>>>>>> d98fb1c44e2d640a5fecdc100702606f65a4875f

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
<<<<<<< HEAD
        self.pushButton.setText(_translate("Form", "PushButton"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
=======
        self.pushButton.setText(_translate("Form", "close"))
        # self.pushButton.setIcon(QIcon("close.png"))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)  # 信号与槽
        self.pushButton.clicked.connect(self.pushButton.close)  # 信号与槽
        self.pushButton.setToolTip("close the widget")
        self.pushButton.setShortcut('Ctrl+D')
        self.pushButton.move(20,20)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
>>>>>>> d98fb1c44e2d640a5fecdc100702606f65a4875f
    sys.exit(app.exec_())