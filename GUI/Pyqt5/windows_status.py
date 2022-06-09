#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: windows_status.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/6/9 9:34
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/6/9 9:34
 * @Descripttion: 
'''

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import win32gui
import win32con
from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


# 看不见的“工具人”窗口类，副窗口
class InvisibleWidget(QWidget):
    def __init__(self, fatherWidget):
        super().__init__()

        # 传入的fatherWidget是主窗口，注意这里主窗口不是副窗口parent
        self.fatherWidget = fatherWidget
        self.setGeometry(-500, -500, 1, 1)
        self.setFixedSize(self.width(), self.height())
        # 设置窗口鼠标事件穿透，相当于不接收鼠标事件
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        # 设置窗口背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 设置窗口为无边框、在任务栏
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # 设置透明度，0为全透明
        self.setWindowOpacity(0)


# 主窗口类
class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setGeometry(400, 300, 400, 500)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # 模拟最小化的按钮
        self.minimizeBtn = QPushButton()

        self.minimizeBtn.setParent(self)
        self.minimizeBtn.setGeometry(20, 20, 40, 30)

        # 当按下minimizeBtn按钮时，执行showMini方法
        self.minimizeBtn.clicked.connect(self.showMini)

        # 副窗口
        self.invisibleWidget = InvisibleWidget(self)
        # self.invisibleWidget.hide()

        # 显示主窗口
        self.show()

        # 获得当前窗口，必须在窗口'show'之后才能获取到，第一个参数是窗口的类名，第二个是标题
        self.hwnd = win32gui.FindWindow("Qt5QWindowIcon", "Timer")


def changeEvent(self, event):
    if event.type() == QEvent.ActivationChange:
        # 当窗口被激活，也就是当用户点击了窗口在任务栏上的图标按钮
        if self.isActiveWindow():
            # showNor是我定义的方法，和showMini对应，相当于显示窗口
            self.showNor()


def showMini(self):
    win32gui.SetWindowPos(self.hwnd, win32con.HWND_BOTTOM, self.x(), self.y(), self.width(), self.height(),
                          win32con.SWP_SHOWWINDOW)
    # 激活一个看不见的窗口，相当于是主窗口失去激活状态
    self.invisibleWidget.activateWindow()


def showNor(self):
    win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, self.x(), self.y(), self.width(), self.height(),
                          win32con.SWP_SHOWWINDOW)


if __name__ == '__main__':
    # 进入 PyQt5 的 UI 循环
    app = QApplication(sys.argv)
    # 创建窗口的实例
    win = MainWin()
    # 退出窗口的条件
    sys.exit(app.exec_())
