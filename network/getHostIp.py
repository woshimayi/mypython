#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: getHostIp.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/19 17:30
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/19 17:30
 * @Descripttion: get host ifname ip
'''

import socket

# 多网卡情况下，根据前缀获取IP
def GetLocalIPByPrefix():
    # print("socket", socket.gethostbyname_ex(socket.gethostname()))
    I = socket.gethostbyname_ex(socket.gethostname())
    return I



if __name__ == '__main__':
    print(GetLocalIPByPrefix())
