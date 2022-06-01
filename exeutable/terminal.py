#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: terminal.py.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/3/22 11:27
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/3/22 11:27
 * @Descripttion: 
'''

import os
from time import sleep

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

print("控制台宽度%d 控制台高度%d" % (width, height))

sleep(3)
# 设置高宽
os.system("mode con cols=230 lines=30")


sleep(3)