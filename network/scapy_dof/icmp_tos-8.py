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
    packet = IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome'
    while True:
        res = sr(packet, iface='lan', timeout=0, verbose=False)
        if res:
            print('[*] ' + host + ' is active')
        time.sleep(1)

def send_ping_vlan(host, vlan):
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    # packet = IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome'
    packet = Ether(dst='8C:44:77:88:44:00') / Dot1Q(vlan=vlan, prio=1) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome'
    while True:
        res = sendp(packet, inter=1/100000, iface='lan')
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

def send_udp_randSrcIp(host, port, dstmac='94:c6:91:02:56:d6'):
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


def send_udp(host, port, dstmac='94:c6:91:02:56:d6'):
    sport = 1000  # 随机产生src port位
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    data = b"welcome aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzwelcome\r\n"
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.4', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet =  Ether(dst='50:11:89:5F:1F:25')/IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=8, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / data
    # packet_1 = IP(src='2010::3', dst=host, tos=8, ttl=64, id=id_ip) / UDP(sport=sport, dport=port) / data
    # packet_1 =  scapy.contrib.igmp.IGMP()
    while True:
        for local_tos in [4, 8]:
            packet =  Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=local_tos, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
            res = sendp(packet, iface='lan')
            if res:
                print('[*] ' + host + ' is active')
        time.sleep(1)


def send_udp_rcv(host, port, dstmac='94:c6:91:02:56:d6'):
    sport = 1000  # 随机产生src port位
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    data = b"welcome aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzwelcome\r\n"
    # ping指令会使用ICMP传输协议,ICMP报文中要封装IP头部
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.4', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    packet =  IP(src='192.168.1.100', dst=host, tos=4, ttl=64, id=id_ip)/UDP(sport=sport, dport=port)/data
    # packet = Ether(dst='24:8B:E0:E5:2D:78')/IP(src='192.168.1.100', dst=host, tos=8, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / data
    # packet_1 = IP(src='2010::3', dst=host, tos=8, ttl=64, id=id_ip) / UDP(sport=sport, dport=port) / data
    # packet_1 =  scapy.contrib.igmp.IGMP()
    while True:
        for local_tos in [5, 8]:
            res = sr1(packet, iface='lan')
            if res:
                print('[*] ' + host + ' is active')
        time.sleep(1)



def send_vlan(host, port, flag = True):
    sport = 2000  # 随机产生src port位
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host, id=id_ip) / UDP(sport=sport, dport=1024) / b'zzzzz'
    # p = IP(tos=2, src='192.168.1.100', dst=host) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host) / ICMP() / b'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(prio=0, vlan=0) / IP(tos=4, src='192.168.1.100', dst=host) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    p = Ether(dst='24:8B:E0:E5:2D:78') / Dot1Q(vlan=6, prio=1) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(vlan=0, prio=4) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'
    # p = Dot1Q(vlan=0) / IP(tos=4, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=sport, dport=port) / b'zzzzzzzzzzzzzzzzzz'

    local_tos = 4
    while True:
        for local_pri in [[1, 2000], [2, 4000]]:
            p = Ether(dst='24:8B:E0:E5:2D:78') / Dot1Q(vlan=6, prio=local_pri[0]) / IP(tos=local_tos, src='192.168.1.100', dst=host, ttl=23) / UDP(sport=local_pri[1], dport=port) / b'zzzzzzzzzzzzzzzzzz'
            res = sendp(p, inter=1/100000, iface='lan')        # 发送带vlan的包必须带iface
            # res = sendpfast(p, pps=1000, loop=1000)
            time.sleep(1)
            try:
                if res:
                    print(res + '|' + host + ' is active')
            except Exception as e:
                print(e)

        if not flag:
            return


def ipv6_pack(dst, port):
    ipv6_packet = IPv6()
    ipv6_packet.src = '3000::7900:7592:4226:c497:fd39'
    ipv6_packet.dst = dst
    ipv6_packet.tc = 32  # Traffic class
    ipv6_packet.fl = 0x12345    # Flow label
    ipv6_packet.nh = 17         # Next header field indicates UDP (17)
    ipv6_packet.port = port
    icmpv6_packet = ICMPv6EchoRequest()
    icmpv6_packet.data = 'Hello, World!'  # ICMPv6 Echo Request message
    ipv6_packet.add_payload(icmpv6_packet)

    while True:
        for tc in [16, 32]:
            ipv6_packet.tc = tc
            icmpv6_packet.data = 'Hello, World!' + str(tc)  # ICMPv6 Echo Request message
            send(ipv6_packet, iface='lan')


def send_ipv6_udp_packet(src_ipv6, dst_ipv6, src_port, dst_port, payload, count=1, iface="lan"):
    """
    发送IPv6 UDP数据包

    参数:
        src_ipv6: 源IPv6地址
        dst_ipv6: 目标IPv6地址
        src_port: 源端口
        dst_port: 目标端口
        payload: UDP负载数据
        count: 发送次数(默认1次)
        iface: 指定网络接口(可选)
    """
    # 构造数据包
    ipv6 = IPv6(src=src_ipv6, dst=dst_ipv6)
    udp = UDP(sport=src_port, dport=dst_port)
    pkt = ipv6 / udp / payload

    while True:
        # 发送数据包
        send(pkt, count=count, iface=iface, verbose=True)
        time.sleep(1)


if __name__ == '__main__':
    print('Hello world')

    # send_ping('180.101.50.242')
    # ipv6_pack("3000::2", 1024)
    # send_ping('180.101.50.242')
    # send_ping('192.168.1.1')
    # send_ping_vlan('192.168.1.1', 100)
    # send_udp('180.101.50.242', 1024)
    # send_udp('180.101.50.242', 1025)
    # send_udp_rcv('180.101.50.242', 53)
    # send_udp('192.168.1.1', 80)
    # send_vlan('180.101.50.242', 8080)
    # send_vlan('180.101.50.242', 8080, False)
    # send_dof('172.16.36.35', '172.16.26.189')
    # send_ipv6_udp_packet("240e:b8f:2b60:900:458a:e08f:2ec9:3dcb", "240e:e9:6002:1ac:0:ff:b07e:36c5", 1024, 1205, "hello world")
    time.sleep(0.1)
    print("exit")
