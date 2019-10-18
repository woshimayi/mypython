# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\zsfile\python27\GUI\Pyqt5\_gride\_gride.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QApplication, QScrollArea

import os, sys

Audio = []
Pictures = [".jpg", ".jepg", ".png", ".gif", ".bmp"]
folder = []
Document = []
Executable = []

dir = r'C:\Users\zs\Pictures'


class Ui_MainWindow(QScrollArea):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.resize(1000, 800)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 创建网络窗口布局
        # self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        # self.gridLayoutWidget.setVisible(True)
        # self.gridLayoutWidget.setObjectName("gridLayoutWidget")


        # 获取显示器分辨率大小
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.desktop_height = self.screenRect.height()
        self.desktop_width = self.screenRect.width()

        # 创建滚动条窗口
        self.topFiller = QtWidgets.QWidget(self.centralWidget)
        self.topFiller.setMinimumSize(self.desktop_width-80, 10000)  # 设置滚动条的尺寸

        # 创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        # 创建布局列表
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.centralWidget.setLayout(self.vbox)

        MainWindow.setCentralWidget(self.centralWidget)

        self.function(dir, Pictures)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def function(self, dir, file):
        print("==========os.walk================")
        index = 1
        print(file)
        positions = [(i*200, j*200) for i in range(100) for j in range(6)]
        for root, dirs, files in os.walk(dir):
            for filepath, position in zip(files, positions):
                if os.path.splitext(filepath)[1] in file:
                    index += 1
                    self.pixmap = QtGui.QPixmap(os.path.join(root, filepath))
                    print(index, position, 'file', os.path.join(root, filepath), self.pixmap.width(), self.pixmap.height())
                    self.pixmap.scaled(
                        self.pixmap.width() / 200,
                        self.pixmap.height() / 200,
                        QtCore.Qt.KeepAspectRatio)

                    if 0 == self.pixmap.width() and 0 == self.pixmap.height():
                        continue
                    width = self.pixmap.width() / 200
                    height = self.pixmap.height() / 200

                    self.label = QtWidgets.QLabel(self.topFiller)
                    self.label.setScaledContents(True)
                    self.label.setObjectName("label")
                    self.label.setText("TextLabel")

                    if width > height:
                        print("width")
                        self.label.setGeometry(
                            *position,
                            self.pixmap.width() / width,
                            self.pixmap.height() / width)
                    else:
                        print("height")
                        self.label.setGeometry(
                            *position,
                            self.pixmap.width() / height,
                            self.pixmap.height() / height)

                    self.label.setPixmap(self.pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
