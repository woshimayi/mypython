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
import logging
import os
import re
import sys
import threading
import xlwt
import xlrd
import time
import xlutils.copy

from Data_storage.json.json_dof import json_Dof

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(funcName)s:line:%(lineno)d] - %(levelname)s:%(message)s')


def json_format(data):
    print(json.dumps(data, sort_keys="True", indent=4, separators=(",", ":")))


class Meminfo(object):
    """docstring for Meminfo"""

    def __init__(self, arg):
        super(Meminfo, self).__init__()
        self.arg = arg
        self.row = 1
        self.file_excl = r'wand_test_record' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.xls'

        self.file_json = r'wand_test_record' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.json'

        self.Host = '192.168.1.1'  # Telnet服务器IP

        self.L = []
        self.M = []

        if self.arg:
            print("SMT")
            self.username = 'telnetadmin'  # 登录用户名
            self.password = 'telnetadmin'  # 登录密码
            self.finish = '#'
        else:
            print("not SMT")
            self.username = 'CMCCAdmin'  # 登录用户名
            self.password = 'aDm8H%MdA'  # 登录密码
            self.finish = '>'

        if os.path.exists(self.file_excl):
            # os.remove(self.file)
            pass
        else:
            workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
            sheet = workbook.add_sheet('share mem', cell_overwrite_ok=True)
            sheet = workbook.add_sheet('meminfo', cell_overwrite_ok=True)
            sheet = workbook.add_sheet('pid mem', cell_overwrite_ok=True)
            workbook.save(self.file_excl)

        # self.start()

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
            time.sleep(1)
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
            elif command == 'bs /b/z':
                # print("zzzzz ", command)
                bs_dict = {}
                flag = 0
                data_par = ''
                dict = {}
                dict_sub = {}
                json_par_key = ''
                for data in str1.split('\r\n'):
                    data = data.strip()
                    # print("space ", len(data), data)

                    if '#' == data:
                        flag = False

                    if 0 == len(data):
                        flag = False
                        continue
                    else:
                        data_par = data

                    if '--------' in data:
                        flag = True
                        dict_sub = {}
                        continue

                    if flag:
                        # logging.debug("%s %s" % (flag, data))
                        pass
                    else:
                        dict[json_par_key] = dict_sub
                        # logging.debug("%s %s" % (flag, data))

                    # logging.debug('%s\t%s' % (flag, data))
                    if '=' in data and flag:
                        dict_sub[data.rsplit('=', 1)[0].strip()] = data.rsplit('=', 1)[1].strip()
                    else:
                        logging.info(data_par)
                        if '=' in data_par:
                            if data_par.rsplit('=', 1)[1].strip().isdigit():
                                json_par_key = data_par
                            else:
                                json_par_key = data_par.rsplit('=', 1)[1].strip()
                        else:
                            logging.debug(data_par)
                            json_par_key = data_par

                # print(dict)
                # print(dict_sub)
                del dict['']
                del dict['bs /b/z']
                print(dict.keys(), len(dict.keys()))
                json_format(dict)
                bs_dict[command] = dict

                j = json_Dof(self.file_json)
                j.add(bs_dict)

                # json_format(dict_sub)

                # self.L = list(dict.keys())
            elif 'mibdump' in command:
                dict_par = {}
                dict_sub = {}
                json_par_key = ''
                for data in str1.splitlines():
                    data = data.strip()
                    # logging.debug(data)
                    if 'Runner Stats' in data:
                        # logging.debug(data)
                        flag = True
                        json_par_key = data.split(':')[1]
                        dict_sub = {}
                        dict_par[json_par_key] = dict_sub
                        continue

                    if ':' in data:
                        # logging.debug(data.rsplit(':', 1))
                        dict_sub[data.rsplit(':', 1)[0]] = data.rsplit(':', 1)[1].strip()
                    else:
                        # logging.debug(data)
                        pass

                dict_json = {}
                dict_json[command] = dict_par
                j = json_Dof(self.file_json)
                j.add(dict_json)


            elif 'bs /b/e port' in command:
                dict = {}
                port_dict = {}
                port_key = command.split('=')[1]
                logging.debug(port_key)
                dict_sub = {}
                for data in str1.split('\r\n'):
                    # logging.info(data)
                    if 'stat' == data.split(':')[0].strip() \
                            or 'debug_stat' == data.split(':')[0].strip() \
                            or 'pkt_size_stat' == data.split(':')[0].strip():
                        # logging.debug(data.split(':')[1].strip())
                        data_sub = data.split(':')[1].strip(' {}')
                        # logging.debug(data_sub)
                        dict_sub = {}
                        for sub in data_sub.split(','):
                            dict_sub[sub.split('=')[0]] = sub.split('=')[1]

                        dict[data.split(':')[0].strip()] = dict_sub

                json_format(dict)

                port_dict[command] = dict

                j = json_Dof(self.file_json)
                j.add(port_dict)


            else:
                dict = self.str2dict(str1)
                self.L = list(dict.keys())
            # print('zzzz', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n', len(dict.keys()), dict)

            # append xml to mem data
            # data = xlrd.open_workbook(self.file_excl)
            # ws = xlutils.copy.copy(data)
            # table = ws.get_sheet(i)
            # table_r = data.sheets()[0]

        #     j = 0
        #     self.row = table_r.nrows
        #     print("j", self.row)
        #     table.write(self.row, 0, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     print("L", type(self.L), self.L)
        #     for key in self.L:
        #         if self.row == 1:
        #             table.write(0, 0, "time")
        #             table.write(0, j, key)
        #
        #         table.write(self.row, j, dict.get(key))
        #         j += 1
        #     ws.save(self.file_excl)
        #     i += 1
        # self.row += 1

        # 执行完毕后，终止Telnet连接（或输入exit退出）
        # tn.read_until(finish.encode())
        tn.close()  # tn.write('exit\n')

        # return dict

    def record(self):
        # commands = ['sh', 'mdm meminfo', 'cat /proc/meminfo', 'showmem']
        # commands = ['sh', 'bs /b/z']
        # commands = ['sh', 'conr add', 'ethswctl -c mibdump -a', 'conr del']
        commands = ['sh',
                    'bs /b/z',
                    'bs /b/c port/index=wan0 pkt_size_stat_en=yes', 'bs /b/e port/index=wan0',
                    'bs /b/e port/index=lan0',
                    'bs /b/e port/index=lan1',
                    'bs /b/e port/index=lan2',
                    'bs /b/e port/index=lan3',
                    'conr add', 'ethswctl -c mibdump -a', 'conr del']

        th = threading.Thread(target=self.do_telnet,
                              args=(self.Host, self.username, self.password, self.finish, commands))
        th.start()
        th.join(5)  # 20秒超时时间 优先执行此线程

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
        commands = ['sh']

        th = threading.Thread(target=self.do_start,
                              args=(self.Host, self.username, self.password, self.finish, commands))
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

    # for i in range(10):
    M.record()
    time.sleep(1)
