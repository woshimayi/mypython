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
    data = xlrd.open_workbook(r'./test.xlsx')
    ws = xlutils.copy.copy(data)
    table = ws.get_sheet(0)

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
        if 'mac addr:' in str1:
            print(str1)
            table.write(i,3, str1)
    ws.save(r'./test.xlsx')
    
    #执行完毕后，终止Telnet连接（或输入exit退出）
    # tn.read_until(finish.encode())
    tn.close() # tn.write('exit\n')

if __name__=='__main__':
    if len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        str = '112233445566'
    print(str)


    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = workbook.add_sheet('test', cell_overwrite_ok=True)

    sheet.write(0,0, 'EnglishName')
    sheet.write(1,0, 'Marcovaldo')
    txt1 = 'CH_ZH'
    sheet.write(0,1, txt1)
    txt2 = 'mamma'
    sheet.write(1, 1, txt2)
    workbook.save(r'./test.xlsx')


    str1 = 'write mac 1 %s%s:%s%s:%s%s:%s%s:%s%s:%s%s\r\n' % (str[0], str[1], str[2], str[3], str[4], str[5], str[6], str[7], str[8], str[9], str[10], str[11])
     # 配置选项
    #pars = replace_db_keyworlds(vars_dict, pars)
    #configs = pars.split(r'@')
    Host = '192.168.1.1' # Telnet服务器IP
    username = 'telnetadmin'   # 登录用户名
    password = 'telnetadmin'  # 登录密码
    finish = 'S304# '      # 命令提示符
    # while 1:
        # str = input('MAC: ')
    print(str)
    str1 = 'write mac 1 %s%s:%s%s:%s%s:%s%s:%s%s:%s%s' % (str[0], str[1], str[2], str[3], str[4], str[5], str[6], str[7], str[8], str[9], str[10], str[11])
    commands = ['manufactory','show mac', str1, 'show mac', 'exit']
    #do_telnet(Host, username, password, finish, commands)
    th1 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
    th1.start()
    th1.join(5)  ##20秒超时时间