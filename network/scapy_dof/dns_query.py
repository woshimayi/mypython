#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: dns_query.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/8/8 16:46
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/8 16:46
 * @Descripttion: dns query request
'''

import sys
import warnings, logging

warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def dns_query(dns_name):
    dns_result = sr1(IP(dst="114.114.114.114") / UDP() / DNS(id=168, qr=0, opcode=0, rd=1, qd=DNSQR(qname=dns_name)),
                     verbose=False)
    # id标识字段（匹配请求与回应），qr等于0标识查询报文，opcode为0表示标准查询，rd为1表示期望递归，qname参数为要查询的域名
    layer = 1
    while True:  # 不太确定DNSRR到底有几组
        try:
            if dns_result.getlayer(DNS).fields['an'][layer].fields['type'] == 1:
                dns_result_ip = dns_result.getlayer(DNS).fields['an'][layer].fields['rdata']
                # 每一层就是一个记录，但是不一定是A，可能是CNAME
                print('域名: {0:<18} 对应的IP地址：{1}'.format(dns_name, dns_result_ip))
            layer += 1
        except:  # 如果超出范围就跳出循环
            break


if __name__ == '__main__':
    print("hello dns")
    dns_query('www.baidu.com')

