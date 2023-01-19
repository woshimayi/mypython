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

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QDateTime, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QMenu, QSystemTrayIcon, QStyle, QAction

from GUI.Pyqt5.wand_test.wand_test import HttpdTest
from GUI.Pyqt5.wand_test.Ui_wand import Ui_Form


class WorkThread(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        num = 0
        be = HttpdTest()
        while True:
            be.wanget_set()
            print("zzzzz", num)
            self.sinOut.emit(str(num))
            num += 1

    def stop(self):
        self.quit()
        self.wait()
        self.terminate()

class WorkTimer(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        self.sinOut.emit('out')

    def stop(self):
        self.quit()
        self.wait()
        self.terminate()


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
        self.num = 0

        # 定时器槽函数
        self.time = QTimer()
        self.time.timeout.connect(self.showTime)
        self.time.start(1 * 1000)

        self.comboBox.addItems([f'{x:02}' for x in range(24)])
        self.comboBox_2.addItems([f'{x:02}' for x in range(60)])

        # 任务栏 start
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            self.style().standardIcon(QStyle.SP_ComputerIcon))

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(QApplication.instance().quit)

        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActived)
        # 任务栏 end

        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('hh:mm')
        print(timeDisplay, timeDisplay.split(':'), type(timeDisplay.split(':')[0]))

        self.comboBox.setCurrentText(timeDisplay.split(':')[0])
        self.comboBox_2.setCurrentText(timeDisplay.split(':')[1])
        self.checkBox.setChecked(False)

        self.runStask.connect(self.stask)

        # self.th = WorkThread()
        # self.th.sinOut.connect(self.append_text)

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
        print(timeDisplay, self.comboBox.currentText() + ':'+ self.comboBox_2.currentText(), self.isrun)
        if self.num < 59 and self.isrun:
            self.num += 1
        else:
            self.num = 0
            self.isrun = False

        if timeDisplay == clock and self.checkBox.isChecked() and False == self.isrun:
            self.textBrowser.append("wand test start")
            self.textBrowser.moveCursor(QTextCursor.End)
            self.isrun = True
            self.runStask.emit('hello')

    def append_text(self, text):
        print(text)
        self.textBrowser.append(text)
        self.textBrowser.moveCursor(QTextCursor.End)

    def stask(self):
        print("ddddddddd")
        try:
            if self.isrun:
                # if self.isMinimized():
                #     self.setWindowState(
                #         self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive | QtCore.Qt.WindowStaysOnTopHint )  # 任何状态下的弹出
                # # elif self.isHidden():
                # else:
                #     self.showNormal()              # 只限再任务栏的弹出

                if self.isHidden():
                    self.showNormal()
                else:
                    self.setWindowState(
                                self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)  # 任何状态下的弹出

                # self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)     # 任何状态下的弹出
                msg_box = QMessageBox.question(self, 'time out', 'wan test', QMessageBox.Yes | QMessageBox.No)
                if msg_box == QMessageBox.Yes or msg_box == QMessageBox.Yes:
                    msg_box.exec_()
                    print("zzzzz true")
                    self.isrun = True
            else:
                pass
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
        self.isrun = False
    
    @pyqtSlot(str)
    def on_comboBox_2_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.checkBox.setChecked(True)
        self.isrun = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = wand()
    ui.show()
    sys.exit(app.exec_())
