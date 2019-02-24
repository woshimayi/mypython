# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button_close.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 91, 101))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
    sys.exit(app.exec_())