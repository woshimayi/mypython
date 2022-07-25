#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: inform_tr69c.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/7/6 18:04
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/7/6 18:04
 * @Descripttion: 
'''
from time import sleep

from reptile.httpd_test.wand_test import HttpdTest
from telnet.telnet_cmcc import Meminfo

informurl = r'http://192.168.1.1/setHbusData?path=hbus://miscd/inform&msgType=214&userTagData=1'

data = {"path": "hbus://miscd/inform", "para": {}}


telnetUrl = 'http://192.168.1.1/setObjs'
enableTelnet = {"TelnetEnable":True,"TelnetWANEnable":False,"TelnetUserName":"CMCCAdmin","TelnetPassword":"aDm8H%MdA","fullPath":"InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage."}
telnetTrue = []
telnetTrue.append(enableTelnet)

if __name__ == '__main__':
    be = HttpdTest()
    M = Meminfo(be.get_region())
    be.post_info(telnetUrl, data=telnetTrue)
    i = 0
    while True:
        be.post_info(informurl, data)
        sleep(3)
        i += 1
        M.record()
        if 100 == i:
            break

    print('Hello world')
