#!/usr/bin/env python3
#encoding=utf-8
"""
Created on Sat Aug 18 22:38:44 2018

@author: zs
"""
#encoding=utf-8

import sys 
import threading
import xlwt
import xlrd
import time
import xlutils.copy



def do_telnet(Host, username, password, finish, commands):
    import telnetlib
    '''Telnet远程登录：Windows客户端连接Linux服务器'''
    # data = xlrd.open_workbook(r'./test.xlsx')
    # ws = xlutils.copy.copy(data)
    # table = ws.get_sheet(0)

    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host, port=23, timeout=10)
    tn.set_debuglevel(2)
    # 输入登录用户名
    tn.read_until('VosLogin: '.encode())
    tn.write(username.encode() + b'\n')
    # 输入登录密码
    tn.read_until('Password: '.encode())
    tn.write(password.encode() + b'\n')
    # 登录完毕后执行命令
    tn.read_until(finish.encode())
    i = 0
    for command in commands:
        #print('cmd')
        i = i+1
        tn.write(b'%s\n' % command.encode())
        time.sleep(0.3)
        str = tn.read_very_eager()
        str1 = '%d %s' % (i, str.strip().decode())

    #执行完毕后，终止Telnet连接（或输入exit退出）
    # tn.read_until(finish.encode())
    tn.close() # tn.write('exit\n')

if __name__=='__main__':
    if len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        str = '112233445566'

    # workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # sheet = workbook.add_sheet('test', cell_overwrite_ok=True)

    Host = '192.168.1.1' # Telnet服务器IP
    username = 'telnetadmin'   # 登录用户名
    password = 'telnetadmin'  # 登录密码

    commands = ['manufactory','show mac', 'exit']
    #do_telnet(Host, username, password, finish, commands)
    finish = 'S304#'
    #
    th1 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th1.start()
    th1.join(5)  ##20秒超时时间

    th2 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th2.start()
    th2.join(5)  ##20秒超时时间

    th3 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th3.start()
    th3.join(5)  ##20秒超时时间

    th4 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th4.start()
    th4.join(5)  ##20秒超时时间

    th5 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th5.start()
    th5.join(5)  ##20秒超时时间