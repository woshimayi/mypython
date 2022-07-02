# -*- coding: utf-8 -*-

"""
Module implementing wand.
"""
import ctypes
import inspect
import sys
import threading

from PyQt5.QtCore import pyqtSlot, QDateTime, QTimer, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication

from GUI.Pyqt5.wand_test.wand_test import HttpdTest
from Ui_wand import Ui_Form


class wand(QWidget, Ui_Form):

    # 其实说到底是因为我们没有定义清楚，pyqt5信号要定义为类属性，而不是放在_init_这个方法里面
    runStask = pyqtSignal(object)
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.isrun = False

        # 定时器槽函数
        self.time = QTimer()
        self.time.timeout.connect(self.showTime)
        self.time.start(1 * 1000)

        self.comboBox.addItems([f'{x:02}' for x in range(24)])
        self.comboBox_2.addItems([f'{x:02}' for x in range(60)])

        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('hh:mm')
        print(timeDisplay, timeDisplay.split(':'), type(timeDisplay.split(':')[0]))

        self.comboBox.setCurrentText(timeDisplay.split(':')[0])
        self.comboBox_2.setCurrentText(timeDisplay.split(':')[1])
        self.checkBox.setChecked(False)

        self.runStask.connect(self.stask)

        self.be = HttpdTest()


    def showTime(self):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        # timeDisplay = time.toString('hh:mm:ss')
        timeDisplay = time.toString('hh:mm')

        clock = self.comboBox.currentText() + ':' + self.comboBox_2.currentText()
        # print(timeDisplay, self.comboBox.currentText() + ':'+ self.comboBox_2.currentText())

        if timeDisplay == clock and self.checkBox.isChecked() and False == self.isrun:
            self.textBrowser.append("wand test start")
            self.textBrowser.moveCursor(QTextCursor.End)
            self.runStask.emit('hello')


    def start_runstask(self, isrun):
        while True:
            if False == isrun:
                self.be.__del__()
                break
            # self.be.wanget_set()
            print("aaaaa")


    def stask(self):
        print("ddddddddd")
        try:
            if self.isrun:
                self.pushButton.setText("START")
                self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
                # self.isrun = False
            else:
                self.pushButton.setText("CANCEL")
                self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
                # self.isrun = True

            self.th = threading.Thread(target=self.start_runstask, args=(self.isrun, ))
            self.th.start()
            self.th.join(5)  # 20秒超时时间
        except Exception as e:
            print(e)


    @pyqtSlot(bool)
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        print(checked)
        if checked:
            self.pushButton.setText("CANCEL")
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.isrun = True
            self.runStask.emit('hello')
        else:
            self.pushButton.setText("START")
            self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.isrun = False
            self.runStask.emit('hello')

    
    @pyqtSlot(str)
    def on_comboBox_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.checkBox.setChecked(True)
    
    @pyqtSlot(str)
    def on_comboBox_2_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.checkBox.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = wand()
    ui.show()
    sys.exit(app.exec_())
