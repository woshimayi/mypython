#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: windows_permission_administrator.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/28 16:32
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/28 16:32
 * @Descripttion:  python 管理员权限运行代码     windows administrator run program
'''

import ctypes, sys, os
from appdirs import unicode


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
    print('Hello world')


    if is_admin():
        # 将要运行的代码加到这里
        os.system('cmd.exe')
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)