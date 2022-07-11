#!/usr/bin/env python
# encoding: utf-8
'''
@author: dof
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: zzzzz@xxx.com
@software: garner
@file: picture_setBrush.py
@time: 2022/07/0003 13:06
@desc:
'''
from PyQt5 import QtWidgets, QtGui

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    windows = QtWidgets.QWidget()
    windows.setWindowTitle('Medusa MQT')
    # 设置背景图片
    window_pale = QtGui.QPalette()
    window_pale.setBrush(windows.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(r"./3.png")))
    windows.setPalette(window_pale)

    windows.setMinimumWidth(400)
    windows.setMaximumWidth(400)
    windows.setMinimumHeight(400)
    windows.setMaximumHeight(400)
    windows.show()
    app.exec_()