#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: 123.py.py
@time: 2020/8/1 15:33
@desc: ssssssssssss
'''

import  os
import sys

import logging

gitinfo = os.popen('git config remote.origin.url')
print(gitinfo.read().strip('\n'))

logging.error("ssss")

