#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: serial-test.py
@time: 2020/8/21 10:39
@desc:
'''
import logging
import threading

import serial

import serial.tools.list_ports


class Serial_My(object):
    """docstring foSerial_Myme"""
    
    def __init__(self):
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        self.portx = "COM1"
        
        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        self.bps = 115200
        
        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        self.timex = None
        
        self.open_port = []
        
        self.serial_find()

    def __del__(self):
        print('__del__')
    
    def serial_find(self):
        self.port_list = list(serial.tools.list_ports.comports())

        if len(self.port_list) == 0:
            print("无可用串口！")
        else:
            for i in range(0, len(self.port_list)):
                print('%d %s' % (i, self.port_list[i]))
                self.open_port.append(str(self.port_list[i]))

        if 1 == len(self.open_port):
            self.portx = self.open_port[0].split(' ')[0]
            self.ser = serial.Serial(self.portx, self.bps, timeout=self.timex)
    
    def serial_read(self):
        try:
            # 读取整行数据
            while True:
                data = str(self.ser.read(), encoding='utf-8')
                data.replace('\n', '\r')
                if 'EX6470 login:' in data or 'Password:' in data:
                    continue
                else:
                    print(data, end='')  # 读一个字节
                # return str(self.ser.readline(), encoding='utf-8').strip('\r\n')
        except Exception as e:
            print("error!", e)
    
    def serial_write(self):
        try:
            while True:
                # 写数据
                data = input()
                if data:
                    # data = data+'\r\n'
                    # data.replace('\r', '\n')
                    # print("sss %s" % bytes(data, encoding='utf-8'))
                    result = self.ser.write(bytes(data, encoding='utf-8'))
                    # result = self.ser.write(bytes('\r\n', encoding='utf-8'))
                    logging.debug("写总字节数：%d", result)
                    data = ''
        except Exception as e:
            print("error!", e)
    
    def serial_close(self):
        self.ser.close()  # 关闭串口


if __name__ == '__main__':
    S = Serial_My()
    th1 = threading.Thread(target=S.serial_read, args='')
    th2 = threading.Thread(target=S.serial_write, args='')
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    
    S.serial_close()
