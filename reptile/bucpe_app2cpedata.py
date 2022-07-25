#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: bucpe_app2cpedata.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/6/7 11:59
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/6/7 11:59
 * @Descripttion: 
'''
import json

import requests

ip = "192.168.1.1"
head = "application/x-www-form-urlencoded; charset=UTF-8"

url = "http://192.168.1.1:17999"
data = {"RPCMethod": "SetLocationInfo", "ID": "101", "Longitude": "110.21", "Latitude": "43.50508", "Elevation": "10",
        "HorizontalError": "65", "AltitudeError": "27", "AreaCode": "112441901001", "TimeStamp": "20220606222448",
        "GISDigest": "9A1B6C7E804A31A6"}


def json_format(data):
    # print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))
    print(json.dumps(data, indent=4, separators=(",", ":")))


class Buapp(object):
    """docstring for Buapp"""

    def __init__(self):
        super(Buapp, self).__init__()
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""
        }

    def post_info(self, url, data):
        try:
            print("\t\tpost", url, data)
            r = requests.post(url, json=data, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                print('\t\t', r.text)
                json_format(r.json())
            print(r.status_code)
        except Exception as e:
            print("error ", e)

    def client_tcp(self, data):
        import socket
        # 1.创建socket
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. 链接服务器
        server_addr = ("192.168.1.1", 17999)
        tcp_socket.connect(server_addr)

        # 3. 发送数据
        send_data = data
        tcp_socket.send(send_data.encode("utf-8"))

        # 4. 关闭套接字
        tcp_socket.close()


if __name__ == '__main__':
    print('Hello world')
    F = Buapp()
    json_format(data)
    # print(data)
    print(json.dumps(data))
    # F.post_info(url, data)
    F.client_tcp(json.dumps(data))
