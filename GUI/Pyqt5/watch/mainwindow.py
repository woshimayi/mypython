# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys

from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def showTime(self):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('hh:mm:ss')
        # 在标签上显示时间
        self.lable.setText(timeDisplay)



    @pyqtSlot(str)
    def on_lcdNumber_windowIconTextChanged(self, iconText):
        """
        Slot documentation goes here.
        
        @param iconText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        print("asdasdasdsa")
        self.lcdNumber.display("ddd")
        # raise NotImplementedError


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())