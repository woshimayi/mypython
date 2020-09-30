# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QWidget, QGridLayout, QDialog, QPushButton
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
        btncont = self.layout.count()
        if 10 < btncont:
            return

        print(btncont)
        label = QLabel(str(btncont)+".jpg", self)
        self.layout.addWidget(label, 0, 1)
        # self.setLayout(self.layout)
        label.setScaledContents(True)
        pixmap = QtGui.QPixmap(str(btncont)+".jpg")

        width =  pixmap.width()/200
        height = pixmap.height()/200

        print(width, height)
        print(pixmap.width(), pixmap.height())

        # if width > height:
        #     print("width")
        #     label.setGeometry(0, 50, pixmap.width()/width, pixmap.height()/width)
        # else:
        #     print("height")
        #     label.setGeometry(0, 50, pixmap.width()/height, pixmap.height()/height)

        label.setPixmap(pixmap)

        self.layout.addWidget(label)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


