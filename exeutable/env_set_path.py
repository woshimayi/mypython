#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: env_set_path.py
@time: 22/10/10 18:02
@desc:
'''

import os
import sys

res = os.path.abspath(__file__)  # 获取当前文件的绝对路径
print(res)
print(os.path.dirname(res))
base_path = os.path.dirname(os.path.dirname(res))  # 获取当前文件的上两级目录
print(base_path)

# sys.path.insert(0, base_path)  # 加入环境变量

# for path in sys.path:
#     print(path)

if __name__ == '__main__':
    print('hello world')
