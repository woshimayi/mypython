#!/usr/bin/env python
# encoding: utf-8
'''
@author: dof
@license: (C) Copyright 2001-2099, Node Supply Chain Manager Corporation Limited. 
@contact: zzzzz@xxx.com
@software: garner
@file: json_treeItem.py
@time: 2022/07/0010 10:53
@desc: 最小化到托盘
'''

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QGridLayout, QWidget,
    QCheckBox, QSystemTrayIcon,
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle)
from PyQt5.uic.properties import QtGui, QtCore


class MainWindow(QMainWindow):
    """
         Сheckbox and system tray icons.
         Will initialize in the constructor.
    """
    tray_icon = None

    # Override the class constructor
    def __init__(self):
        # Be sure to call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(480, 80))  # Set sizes
        self.setWindowTitle("System Tray Application")  # Set a title

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        # 设置托盘图标
        self.tray_icon.setIcon(
            self.style().standardIcon(QStyle.SP_ComputerIcon))

        '''
            Define and add steps to work with the system tray icon
            show - show window
            hide - hide window
            exit - exit from application
        '''
        # show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        # hide_action = QAction("Hide", self)
        # show_action.triggered.connect(self.show)
        # hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(QApplication.instance().quit)

        tray_menu = QMenu()
        # tray_menu.addAction(show_action)
        # tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActived)

    # Override closeEvent, to intercept the window closing event
    # The window will be closed only if there is no check mark in the check box
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
            if self.isHidden():
                # self.show()
                self.showNormal()
            else:
                self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
