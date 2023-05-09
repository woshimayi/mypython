#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: igmp_send.py
@time: 23/4/28 15:52
@desc:
'''


# from scapy.all import *
from scapy.arch import get_windows_if_list
from scapy.contrib.igmp import IGMP
# import random

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp

src_ip = "192.168.1.100"
multicast_ip = "239.255.12.45"
interface = "eth0"

def send_igmp_report(ifname, srcIP='192.168.1.100', dstIP='239.1.2.3', srcmac='94:c6:91:02:56:d6', dstmac='01:00:5e:01:01:02'):
    try:
        a=Ether(src=srcmac, dst=dstmac)
        b=IP(src=srcIP, dst=dstIP)
        c=IGMP(type=0x16, gaddr=dstIP)
        sendp(a/b/c, iface=ifname)
    except Exception as e:
            print(e)


if __name__ == '__main__':
    ifname_list = get_windows_if_list()
    print(ifname_list)
    index = 0
    ifname = ''
    srcmac = ''
    dstmac = ''
    srcIP = ''
    dstIP = ''

    for iface in ifname_list:
        if iface['ips']:
            print(iface['index'], ' : ', iface['name'])
    index = input("input ifname index : ")
    for _iface in ifname_list:
        # print(_iface['name'], _iface['index'], _iface['ips'][0])
        if int(index) == _iface['index']:
            ifname = _iface['name']
            srcIP = _iface['ips'][0]
            srcmac = _iface["mac"]
            break
    dstmac = input("input dst mac     : ")
    dstIP =  input("input dst  ip     : ")
    print(index, ifname, dstmac, srcIP, dstIP)

    while True:
        send_igmp_report(ifname, srcIP, dstIP, srcmac, dstmac)
        input("please input Enter.. : ")

        print('hello world')