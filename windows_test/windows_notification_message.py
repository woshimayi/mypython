#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: windows_notification_message.py
@time: 23/6/6 14:38
@desc:  windows 10 系统右下角弹窗
'''


from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("这是一个测试消息",
                   "从前有只羊，它一直在山上吃草，后来有一天它不见了",
                   icon_path="f.ico",
                   duration=5)

if __name__ == '__main__':
    print('hello world')
