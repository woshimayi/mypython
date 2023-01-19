#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: ipy_test.py
@time: 23/1/18 13:50
@desc: ip 掩码 网段  数量 计算
'''


from IPy import *


# print(IP('192.168.147.0/32').strNormal(3))
# print(IP('192.168.147.0/31').strNormal(3))
# print(IP('192.168.147.0/30').strNormal(3))
# print(IP('192.168.147.0/29').strNormal(3))

# ip = IP('192.168.147./26')
# print(ip.len())
# print(IP('192.168.147.128/26').strNormal(3))


# print(IP('192.168.147.0/23').overlaps('192.168.145.0/24'))



#  计算ip 数量 和范围
for i in range(32, 1, -1):
    try:
        str_ip = '192.168.0.0/' + str(i)
        # print(IP(str_ip).strNormal(3))
        # print(str_ip)
        ip = IP(str_ip)
        print("%2d: %10d %s-%s" % (i, ip.len(), ip[0], ip[-1]))
    except Exception as e:
        pass




# ip = IP('192.168.147.192/27').strNormal(3)
# print(ip.len())
# ip = IP('192.168.147.224/27').strNormal(3)
# print(ip.len())

# print(IP('192.168.147.158').strBin())
# print(IP('192.168.147.162').strBin())
# print(IP('192.168.147.158').strHex() & IP('255.255.255.0').strHex())
print(bin((0b11000000101010001001001110011110 & 0b11000000101010001001001110100010)))




if __name__ == '__main__':
    print('hello world')
