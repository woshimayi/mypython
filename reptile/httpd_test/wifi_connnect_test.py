#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: wifi_connnect_test.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/8/23 17:57
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/23 17:57
 * @Descripttion: 
'''
import ctypes
import os
import sys
import time
from time import sleep
import pywifi
import requests
from pywifi import const


# current_path = os.getcwd()
# print(current_path)
# sys.path.append(r'T:/mypython')

from Data_storage.json.json_dof import json_Dof

url_conn = r'https://www.sina.com.cn/'
download_url = r'http://192.168.60.252:8080/QQ8.7.exe'

# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)

class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


class WifiTest:
    """docstring for WifiTest"""

    def __init__(self):
        print("start")
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""
        }

        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]  # 取一个无线网卡

        self.conn_success = 0
        self.conn_fail = 0
        self.conn_fail_continue = 0

    def wifi_connect(self, ssid, password='12345678'):
        try:
            print('\t\t' + time.strftime("%Y%m%d-%H:%M:%S", time.localtime()) + '    ', end='',flush=True)
            conn_fail_continue_tmp = 0
            flag = False

            self.iface.remove_all_network_profiles()
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN  # 需要秘密
            profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
            profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
            profile.key = password
            sleep(2)

            profile = self.iface.add_network_profile(profile)

            while True:
                self.iface.connect(profile)
                sleep(4)  # 程序休眠时间3秒；如果没有此句，则会打印连接失败，因为它需要一定的检测时间
                if self.iface.status() == const.IFACE_CONNECTED:
                    self.conn_success += 1
                    self.conn_fail_continue = 0
                    # if (self.conn_fail + self.conn_success) == 0:
                    #     self.perent = 0.0000
                    # else:
                    #     self.perent = self.conn_fail / (self.conn_fail + self.conn_success)*100
                    # print("连接成功 ! ! !  成功: %d 失败: %d  失败率: %% %f" % (self.conn_success, self.conn_fail, self.perent), flush=True)
                    # print("连接成功 ! ! !", end='')
                    flag = True
                    break
                elif self.iface.status() == const.IFACE_CONNECTING:
                    conn_fail_continue_tmp += 1
                    if conn_fail_continue_tmp >= 3:
                        self.conn_fail += 1
                        self.conn_fail_continue += 1
                        # if (self.conn_fail + self.conn_success) == 0:
                        #     self.perent = 0.000
                        # else:
                        #     self.perent = self.conn_fail / (self.conn_fail + self.conn_success) * 100
                        # print("连接失败 ! ! !  成功: %d 失败: %d  失败率: %% %f \t\t\t 连续失败次数: %d" % (self.conn_success, self.conn_fail, self.perent, self.conn_fail_continue), flush=True)
                        # print("连接失败 ! ! !", end='')
                        flag = False
                        break
                    else:
                        continue
                else:
                    self.conn_fail += 1
                    self.conn_fail_continue += 1
                    # if (self.conn_fail + self.conn_success) == 0:
                    #     self.perent = 0.0000
                    # else:
                    #     self.perent = self.conn_fail / (self.conn_fail + self.conn_success) * 100
                    # print("连接失败 ! ! !  成功: %d 失败: %d  失败率: %% %f result: %d\t\t\t 连续失败次数: %d" % (self.conn_success, self.conn_fail, self.perent, self.iface.status(), self.conn_fail_continue), flush=True)
                    # print("连接失败 ! ! !", end='')
                    flag = False
                    break

            if (self.conn_fail + self.conn_success) == 0:
                self.perent = 0.0000
            else:
                self.perent = self.conn_fail / (self.conn_fail + self.conn_success) * 100

            if flag:
                print("连接成功 ! ! !  成功: %d 失败: %d  失败率: %% %f" % (self.conn_success, self.conn_fail, self.perent),
                      flush=True)
                return True
            else:
                print("连接失败 ! ! !  成功: %d 失败: %d  失败率: %% %f result: %d \t\t\t 连续失败次数: %d" % (
                self.conn_success, self.conn_fail, self.perent, self.iface.status(), self.conn_fail_continue), flush=True)
                return False

        except Exception as e:
            print('wifi connect error', e,flush=True)

    def get_url(self, url=url_conn):
        try:
            print('\t\t' + time.strftime("%Y%m%d-%H:%M:%S", time.localtime()) + '    ', end='',flush=True)
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                print("%s connected success" % (url),flush=True)
                return 0
            else:
                print("%s connected fail" % (url),flush=True)
        except Exception as e:
            print(e)

    def download(self, url=download_url):
        try:
            print('\t\t' + time.strftime("%Y%m%d-%H:%M:%S", time.localtime()) + '    ', end='',flush=True)
            tmp_file = r'QQ.exe'
            if os.access(tmp_file, os.F_OK):
                os.remove(tmp_file)

            r = requests.get(url, headers=self.headers, timeout=20, stream=True)
            size = r.headers.get('Content-Length')
            j = 1
            if 200 == r.status_code:
                print('connect download url success', url, end='',flush=True)
                with open(tmp_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=512):
                        f.write(chunk)
                        # print('.', end='', flush=True)

                    f.close()
                    print(" download success",flush=True)
            else:
                print('connect download url fail', url,flush=True)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    w = WifiTest()

    log_file = r'wifi_test_record' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.log'
    if os.access(log_file, os.F_OK):
        os.remove(log_file)
    sys.stdout = Logger(log_file)

    os.system("route delete 172.16.80.4")
    os.system("route add -p 172.16.80.4 mask 255.255.255.255 192.168.1.1 if ")

    wifi_cfg = "wifi_cfg.json"
    if not os.access(wifi_cfg, os.F_OK):
        print("not wifi_cfg.json file",flush=True)
        f = open(wifi_cfg, 'w')
        f.write("[]")
        f.close()
        obj = [{"url_conn": "http://172.16.80.4/anysize/100k", "download_url": "http://172.16.80.4/anysize/100k",
                "ssid": ["CMCC-zszs-5G"], "password": "12345678"}]

        j = json_Dof(wifi_cfg)
        j.add(obj)
    else:
        j = json_Dof(wifi_cfg)

    url_conn = j.find('url_conn')[0]
    download_url = j.find('download_url')[0]
    password_ssid =  j.find('password')[0]
    L = j.find('ssid')
    print("ssids: ", L)
    ssids = j.find('ssid')[0]

    print("    url_conn: ", url_conn, flush=True)
    print("download_url: ", download_url, flush=True)
    print("       ssids: ", ssids,flush=True)
    print("    password: ", password_ssid, flush=True)

    i = 0
    while True:
        # 将日志输出到指定路径
        print("第%d次连接 " % i,end='', flush=True)
        # sleep(3)

        # test code
        # j = json_Dof(wifi_cfg)
        # password_ssid = j.find('password')[0]


        for ssid in ssids:
            print(ssid)
            sleep(1)
            ret = w.wifi_connect(ssid, password_ssid)  # 填写连接的SSID，和密码，这里加密方式用的WPA2-PSK，其它加密方式可以修改配置文件
            if ret:
                sleep(2)
                w.get_url(url=url_conn)
                sleep(0.3)
                w.download(url=download_url)
        sys.stdout.flush()
        i += 1

    print('Hello world')

