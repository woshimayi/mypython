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
import json
import socket
import  platform
import netifaces
import pprint

def json_format(data):
    print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))

# 多网卡情况下，根据前缀获取IP
def GetLocalIP():
    system = platform.system()
    print("system", system)
    I = []
    try:
        if system == "Windows":
            import winreg as wr
            I = socket.gethostbyname_ex(socket.gethostname())[2]
            # pp = pprint.PrettyPrinter(indent=4)
            # ifnames = netifaces.interfaces()
            # print("zzzzz", ifnames)
            # for ifname in ifnames:
            #     # ifname = get_key(ifname)
            #     print("zzzzz", ifname)
            #     ifnameip = netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
            #     print(ifname, ifnameip)
        elif system == "Linux":
            pp = pprint.PrettyPrinter(indent=4)
            ifnames = netifaces.interfaces()
            for ifname in ifnames:
                ifnameip = netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
                data1 = json.dumps(
                    {ifname: ifnameip},
                    ensure_ascii=True,
                    indent=4,
                    separators=(
                        ',',
                        ':'))
                # print(json.loads(data1))
                I.append(json.loads(data1))
        return I
    except:
        pass

if __name__ == '__main__':
    json_format(GetLocalIP())
