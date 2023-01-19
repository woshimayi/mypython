# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button_close.ui'
#
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(60, 40, 91, 101))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 170, 200, 110))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    sys.exit(app.exec_())