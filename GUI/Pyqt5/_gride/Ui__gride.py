# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\zsfile\python27\GUI\Pyqt5\_gride\_gride.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.gridLayoutWidget.setVisible(True)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        MainWindow.setCentralWidget(self.centralWidget)

        positons = [(i*200, j*200) for i in range(5) for j in range(2)]

        for positon, i in zip(positons, range(1, 10)):
            self.pixmap =  QtGui.QPixmap(str(i) + ".jpg")
            print(self.pixmap.width(), self.pixmap.height())

            width = self.pixmap.width() / 200
            height = self.pixmap.height() / 200

            print(width, height)
            print(self.pixmap.width(), self.pixmap.height())

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.label.setText("TextLabel")
            if width > height:
                print("width")
                self.label.setGeometry(*positon, self.pixmap.width()/width, self.pixmap.height()/width)
            else:
                print("height")
                self.label.setGeometry(*positon, self.pixmap.width()/height, self.pixmap.height()/height)

            self.pixmap.scaled(self.pixmap.width(), self.pixmap.height(), QtCore.Qt.IgnoreAspectRatio)

            self.label.setPixmap(self.pixmap)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
