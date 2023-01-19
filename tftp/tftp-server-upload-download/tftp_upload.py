#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: tftp_upload.py
@time: 20/12/8 19:16
@desc: 
'''



#!/usr/bin/env python3
#coding=utf-8

import struct
from socket import *


def tftp_upload(filename, server_ip, port):
    if '' == filename or '' == server_ip:
        print('pls input filename or server ip')
        return 0
    if '' == port:
        port = 69
    print(filename, server_ip, port)
    send_data_1 = struct.pack('!H8sb5sb',2,filename.encode('gb2312'),0,b'octet',0)
    s = socket(AF_INET,SOCK_DGRAM)
    s.sendto(send_data_1,(server_ip,port)) #第一次发给服务器69端口
    
    f = open(filename,'rb')
    
    recv_data = s.recvfrom(1024) #第一次接收数据
    rand_port = recv_data[1][1]
    print()
    ack_num = struct.unpack("!HH",recv_data[0][:4])
    num = 0
    
    while True:
        read_data = f.read(512)
        send_data = struct.pack('!HH',3,num) + read_data
        s.sendto(send_data,(server_ip,rand_port)) #第二次发给服务器的随机端口
        recv_data_2,userinfo = s.recvfrom(1024)
        print(recv_data_2)
        ack_num = struct.unpack('!H',recv_data_2[2:4])
        print(len(read_data),num,ack_num[0],rand_port)
        if len(read_data) < 512 or ack_num[0] != num :
            break
        num = num + 1
        
if __name__ == '__main__':
    tftp_upload('123.bin', '192.168.1.101', 69)
