#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: icmp_tos.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited.
 * @Author: dof
 * @Date: 2022/8/3 17:44
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/3 17:44
 * @Descripttion:
'''
import time
from random import randint
from scapy.all import *
import scapy.contrib.igmp

# self.th = Process(target=start_runstask)
# self.th.start()
from scapy.layers.inet import IP, UDP
from scapy.layers.inet6 import ICMPv6EchoRequest, IPv6
from scapy.layers.l2 import Dot1Q, Ether


import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def send_ping(host):
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    packet = Dot1Q(vlan=0) /IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome'
    while True:
        res = sr1(packet, iface='lan', timeout=0, verbose=False)
        if res:
            print('[*] ' + host + ' is active')
            time.sleep(1)


def send_dof(src, host):
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    packet = IP(src=src, dst=host, tos=4, ttl=64, id=id_ip, proto=155) / b'welcome'
    while True:
        res = sr1(packet, iface='offic', timeout=0, verbose=False)
        if res:
            print('[*] ' + host + ' is active')
        time.sleep(1)

def send_udp(host, port, dstmac='94:c6:91:02:56:d6'):
    sport = 1000  # 随机产生src port位
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    data = b"welcome aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzwelcome\r\n"
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.4', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='f8:b1:56:c1:0e:37')/IP(src='172.16.37.124', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.2', dst=host, tos=8, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / data
    # packet_1 = IP(src='2010::3', dst=host, tos=8, ttl=64, id=id_ip) / UDP(sport=sport, dport=port) / data
    # packet_1 =  scapy.contrib.igmp.IGMP()
    srcmac = "00:11:22:33:44:"
    i=0
    srcip = '192.168.1.2'
    while True:
        # res = send(packet)
        srcmac = "%s%02x" % ('00:11:22:33:44:', i)
        srcip = "192.168.1.%d" % (i)
        packet = Ether(src=srcmac, dst='24:8B:E0:E5:2D:78')/IP(src=srcip, dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
        # res = sendp(packet, iface='lan')
        res = sendp(packet, iface='lan')
        time.sleep(1)
        i = i+1
        if i >= 0xff:
            i=0
        if res:
            print('[*] ' + host + ' is active')


def send_vlan(host, port):
    sport = 2000  # 随机产生src port位
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host, id=id_ip) / UDP(sport=sport, dport=1024) / b'zzzzz'
    # p = IP(tos=2, src='192.168.1.100', dst=host) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host) / ICMP() / b'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    p = Ether(dst='24:8B:E0:E5:2D:78') / Dot1Q(vlan=0, prio=3) / IP(tos=4, src='192.168.1.2', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(vlan=0, prio=4) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(vlan=0) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'

    while True:
        res = sendp(p, inter=1/100000, iface='wlan')        # 发送带vlan的包必须带iface
        # res = sendpfast(p, pps=1000, loop=1000)
        time.sleep(1)
        try:
            if res:
                print(res + '|' + host + ' is active')
        except Exception as e:
            print(e)

def ipv6_pack():
    ipv6_packet = IPv6()
    ipv6_packet.src = '3000::6100:de84:d70a:2983:1352'
    ipv6_packet.dst = '3000::2'
    ipv6_packet.tc = 14  # Traffic class
    ipv6_packet.fl = 0x12345    # Flow label
    ipv6_packet.nh = 17         # Next header field indicates UDP (17)
    icmpv6_packet = ICMPv6EchoRequest()
    icmpv6_packet.data = 'Hello, World!'  # ICMPv6 Echo Request message
    ipv6_packet.add_payload(icmpv6_packet)

    while True:
        send(ipv6_packet, iface='lan')


if __name__ == '__main__':
    print('Hello world')

    # send_ping('180.101.50.242')
    # ipv6_pack()
    # send_ping('180.101.50.242')
    # send_udp('180.101.49.13', 1024)
    # send_udp('180.101.49.13', 1025)
    send_udp('192.168.1.1', 80)
    # send_vlan('180.101.50.242', 8080)
    # send_dof('172.16.36.35', '172.16.26.189')
    time.sleep(0.1)
    print("exit")
