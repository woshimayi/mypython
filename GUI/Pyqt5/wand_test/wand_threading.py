# -*- coding: utf-8 -*-

"""
Module implementing wand.
"""
import ctypes
import inspect
import sys
import threading
import time
from multiprocessing import Process

from PyQt5.QtCore import pyqtSlot, QDateTime, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication, QStyle, QSystemTrayIcon, QAction, QMenu

from GUI.Pyqt5.wand_test.Ui_wand import Ui_Form
from GUI.Pyqt5.wand_test.wand_test import HttpdTest
# from Ui_wand import Ui_Form


class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.be = HttpdTest()

    def run(self):

        # target function of the thread class
        try:
            while True:
                print('running ' + self.name)
                self.be.wanget_set()

        finally:
            print('ended')

    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


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
        self.th = ''

        # 任务栏
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            self.style().standardIcon(QStyle.SP_ComputerIcon))
        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(QApplication.instance().quit)

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActived)

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

    # 关闭窗口事件 重写
    def closeEvent(self, event):
        print("aaaa")
        event.ignore()
        self.hide()
        # self.tray_icon.showMessage(
        #     "Tray Program",
        #     "Application was minimized to Tray",
        #     QSystemTrayIcon.Information,
        #     2000
        # )

    # 双击托盘图标还原程序
    def iconActived(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden() or self.isMinimized():
                # self.show()
                self.showNormal()
            else:
                self.hide()



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

            self.pushButton.setText("CANCEL")
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")

            self.isrun = True
            self.runStask.emit('hello')

    def stask(self):
        print("ddddddddd")
        try:
            if self.isrun:
                self.th = thread_with_exception('Thread 1')
                self.th.start()
            else:
                self.th.raise_exception()

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
            self.checkBox.setChecked(False)
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
