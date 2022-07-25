#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# coding: utf-8
"""
Created on Sat Aug 18 22:38:44 2018

@author: zs
"""
# encoding=utf-8
import datetime
import json
import os
import sys
import threading
import xlwt
import xlrd
import time
import xlutils.copy



class Meminfo(object):
    """docstring for Meminfo"""

    def __init__(self, arg):
        super(Meminfo, self).__init__()
        self.arg = arg
        self.row = 1
        self.file = r'wand_test_record' + time.strftime("%Y%m%d", time.localtime()) + '.xls'

        self.Host = '192.168.1.1'  # Telnet服务器IP

        self.L = []
        self.M = []

        if self.arg:
            self.username = 'telnetadmin'  # 登录用户名
            self.password = 'telnetadmin'  # 登录密码
            self.finish = '#'
        else:
            self.username = 'CMCCAdmin'  # 登录用户名
            self.password = 'aDm8H%MdA'  # 登录密码
            self.finish = '>'


        if os.path.exists(self.file):
            os.remove(self.file)
        workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = workbook.add_sheet('share mem', cell_overwrite_ok=True)
        sheet = workbook.add_sheet('meminfo', cell_overwrite_ok=True)
        sheet = workbook.add_sheet('pid mem', cell_overwrite_ok=True)
        workbook.save(self.file)

        self.start()



    def str2dict(self, str):
        dict = {}
        for data in str.splitlines():
            if ':' in data:
                dict[data.split(':')[0].strip()] = data.split(':')[1].strip(' kB')
        return dict

    def str2dict_3(self, str):
        dict = {}
        for data in str.splitlines():
            if ' ' in data:
                dict[data.split(' ')[1].strip()] = data.split(' ')[2].strip()
        return dict

    def do_telnet(self, Host, username, password, finish, commands):
        import telnetlib
        '''Telnet远程登录：Windows客户端连接Linux服务器'''

        # 连接Telnet服务器
        tn = telnetlib.Telnet(Host, port=23, timeout=2)
        tn.set_debuglevel(0)

        # 输入登录用户名
        tn.read_until('Login: '.encode())
        tn.write(username.encode() + b'\n')

        # 输入登录密码
        tn.read_until('Password: '.encode())
        tn.write(password.encode() + b'\n')

        # 登录完毕后执行命令
        tn.read_until(finish.encode())

        i = 0
        for command in commands:
            # print('cmd', command)
            tn.write(b'%s\n' % command.encode())
            time.sleep(0.3)
            str = tn.read_very_eager()
            str1 = '%s' % (str.strip().decode('ascii'))
            # print(str1.splitlines()[1].strip('#'))
            print(str1)
            if command == 'sh':
                continue
            elif command == 'showmem':
                dict = self.str2dict_3(str1)
                new_sys = dict.keys()
                print("dict", new_sys)
                print('zzzzz 0', self.M)
                if 0 == len(self.M):
                    self.M = list(dict.keys())
                self.L = self.M
                with open("dict_record.txt", 'a+') as f:
                    f.write(' , '.join(new_sys) + '\n')
                    f.close()
            else:
                dict = self.str2dict(str1)
                self.L = list(dict.keys())
            print('zzzz', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n', len(dict.keys()), dict)

            # append xml to mem data
            data = xlrd.open_workbook(self.file)
            ws = xlutils.copy.copy(data)
            table = ws.get_sheet(i)

            j = 1
            table.write(self.row, 0, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("L", type(self.L), self.L)
            for key in self.L:
                if self.row == 1:
                    table.write(0, 0, "time")
                    table.write(0, j, key)

                table.write(self.row, j, dict.get(key))
                j += 1
            ws.save(self.file)
            i += 1
        self.row += 1

        # 执行完毕后，终止Telnet连接（或输入exit退出）
        # tn.read_until(finish.encode())
        tn.close()  # tn.write('exit\n')

        return dict

    def record(self):
        commands = ['sh', 'mdm meminfo', 'cat /proc/meminfo', 'showmem']

        th = threading.Thread(target=self.do_telnet, args=(self.Host, self.username, self.password, self.finish, commands))
        th.start()
        th.join(5)  # 20秒超时时间


    def do_start(self, Host, username, password, finish, commands):
        import telnetlib
        '''Telnet远程登录：Windows客户端连接Linux服务器'''

        # 连接Telnet服务器
        tn = telnetlib.Telnet(Host, port=23, timeout=10)
        tn.set_debuglevel(0)
        # 输入登录用户名
        tn.read_until('Login: '.encode())
        tn.write(username.encode() + b'\n')
        # 输入登录密码
        tn.read_until('Password: '.encode())
        tn.write(password.encode() + b'\n')
        # 登录完毕后执行命令
        tn.read_until(finish.encode())
        i = 0
        for command in commands:
            # print('cmd', command)
            i = i + 1
            tn.write(b'%s\n' % command.encode())
            time.sleep(0.3)
            str = tn.read_very_eager()
            str1 = '%d %s' % (i, str.strip().decode())
            print(str1)

        # 执行完毕后，终止Telnet连接（或输入exit退出）
        # tn.read_until(finish.encode())
        tn.close()  # tn.write('exit\n')

    def start(self):
        commands = ['sh', 'echo 1 > /tmp/enable_tylog']

        th = threading.Thread(target=self.do_start, args=(self.Host, self.username, self.password, self.finish, commands))
        th.start()
        th.join(5)  # 20秒超时时间



if __name__ == '__main__':
    if len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        str = '112233445566'


    M = Meminfo(False)
    if os.path.exists("dict_record.txt"):
        os.remove("dict_record.txt")

    for i in range(10):
        M.record()
        time.sleep(1)
