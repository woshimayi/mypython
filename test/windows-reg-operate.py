#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: windows-reg-operate.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/28 14:37
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/28 14:37
 * @Descripttion: 
'''

import winreg
# from __future__ import print_function
import ctypes, sys
from appdirs import unicode


# key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell")

# 获取该键的所有键值，因为没有方法可以获取键值的个数，所以只能用这种方法进行遍历

# try:
#     i = 0
#     while 1:
#         # EnumValue方法用来枚举键值，EnumKey用来枚举子键
#         # name, value, type = winreg.EnumValue(key, i)
#         # print(repr(name), repr(value), repr(type))
#         name = winreg.EnumKey(key, i)
#         print(name.splitlines()[0])
#         i += 1
# except WindowsError:
#     print(WindowsError)
# 如果知道键的名称，也可以直接取值
# value, type = winreg.QueryValueEx(key, "EnableAutoTray")
# path=winreg.QueryValueEx(key,'Icon')
# print('path', repr(path))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def reg_test():
    key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"*\shell", access=winreg.KEY_ALL_ACCESS)

    # 创建新的键

    newKey = winreg.CreateKey(key, "send email")

    # 给新创建的键添加键值

    winreg.SetValueEx(newKey, "", 0, winreg.REG_SZ, "aaa")

    winreg.SetValueEx(newKey, "b1", "star", 1, "bbb")

    # 创建新的子键

    key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"*\shell\send email")

    newKey = winreg.CreateKey(key, "DefaultIcon")

    winreg.SetValueEx(newKey, "", 0, winreg.REG_EXPAND_SZ, "path ,1")

    newKey = winreg.CreateKey(key, "shell")

    key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"send email\shell")

    newKey = winreg.CreateKey(key, "open")

    key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"send email\shell\open")

    newKey = winreg.CreateKey(key, "command")

    winreg.SetValueEx(newKey, "url", 0, winreg.REG_EXPAND_SZ, "\"path\" \"%1\"")

def add_reg():
    obj = 'send email'
    obj_key = 'Icon'
    sub_obj = 'command'
    sub_obj_key = 'Icon'

    key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"*\shell", 0, access=winreg.KEY_ALL_ACCESS)

    # 创建新的键
    newKey = winreg.CreateKey(key, obj)
    # 给新创建的键添加键值
    winreg.SetValueEx(newKey, obj_key, 0, winreg.REG_SZ, r"E:\tools\send-email\main.py")
    # 注册表中 (默认) 等值为 ""
    winreg.SetValueEx(newKey, "", 0, winreg.REG_SZ, "发送邮件")

    # 创建新的子键
    newKey = winreg.CreateKey(newKey, sub_obj)
    # 给新创建的键添加键值
    winreg.SetValueEx(newKey, "", 0, winreg.REG_SZ, r"D:\soft\Anaconda3\pythonw.exe E:\tools\send-email\main.py %1")

def show_regs():
    i = 0
    regsKey = []
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell")
        while 1:
            # 读取注册表键
            name = winreg.EnumKey(key, i)
            regsKey.append(name)
            i += 1
    except WindowsError as e:
        print(e)
        # pass

    print('regsKey', regsKey)
    for tmp_key in regsKey:
        print(tmp_key)
        try:
            reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\\" + tmp_key)
            i = 0
            while 1:
                name, value, type = winreg.EnumValue(reg, i)
                print("\t [%s] [%s] [%s]" % (name, value, type))
                reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\\" + tmp_key + '\\' + name)
                print("\t\t %s" % name)
                while 1:
                    name, value, type = winreg.EnumValue(reg, i)
                    print("\t [%s] [%s] [%s]" % (name, value, type))
                    i += 1
                i += 1
        except WindowsError as e:
            print(e)
            # pass
        print()

if __name__ == '__main__':
    print('Hello world')


    show_regs()

    # if is_admin():
    #     add_reg()
    # else:
    #     if sys.version_info[0] == 3:
    #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #     else:  # in python2.x
    #         ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
