# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QWidget
from PyQt5 import QtGui, QtCore
from Ui_list import Ui_MainWindow

import sys
from bs4 import BeautifulSoup
import  requests
import time

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
        'authorization': ""
        }

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        # r = requests.get('https://cn.bing.com/', headers=headers)
        # r.encoding='utf-8'
        # soup=BeautifulSoup(r.text,"lxml")
        # img = requests.get('https://cn.bing.com' + soup.link.get('href'))
        # jpg = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + '.jpg'
        # print(jpg)
        # f = open(jpg, 'wb')
        # f.write(img.content)
        # f.close()
        # 
        self.label = QLabel()
        self.label.setGeometry(160, 90, 0, 0)
        self.label.setObjectName("label")
        self.label.setText("sssssssssss")

        self.pixmap = QtGui.QPixmap("10.jpg")

        self.width = self.pixmap.width()/200
        self.height = self.pixmap.height()/200

        print(self.width, self.height)

        if self.width > self.height:
            print("width")
            self.label.setGeometry(0, 50, self.pixmap.width()/self.width, self.pixmap.height()/self.width)
        else:
            print("height")
            self.label.setGeometry(0, 50, self.pixmap.width()/self.height, self.pixmap.height()/self.height)

        self.label.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

