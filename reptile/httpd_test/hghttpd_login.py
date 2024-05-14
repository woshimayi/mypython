#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited.
@contact: woshidamayi@gmail.com
@software: dof
@file: hghttpd_login.py.py
@time: 24/3/27 20:26
@desc:
'''

import json
import time
from time import sleep
import telnetlib

import requests
import sys
import os
from bs4 import BeautifulSoup

from telnet.telnet_cmcc import Meminfo

ip = "192.168.1.1"
head = "application/x-www-form-urlencoded; charset=UTF-8"

action_1 = {
    'cmdType': 'wanConnection',
    'para': {
        'wanIndex': [1]
    }
}

action_2 = {
    'cmdType': 'wanConnection',
    'para': {
        'wanIndex': [2]
    }
}

add_int = {"path": "hbus://wan/editWan",
           "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                    "802-1pMark": 0, "LanInterface-DHCPEnable": 1, "IPMode": 1, "NATEnabled": True, "MTU": 1460,
                    "ConnectionType": "IP_Routed", "AddressingType": "DHCP", "ServiceList": "INTERNET"}}

add_tr69 = {"path": "hbus://wan/editWan",
            "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                     "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1460, "ConnectionType": "IP_Routed",
                     "AddressingType": "DHCP", "ServiceList": "TR069"}}
add_voip = {"path": "hbus://wan/editWan",
            "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                     "802-1pMark": 0, "IPMode": 1, "MTU": 1460, "ConnectionType": "IP_Routed", "AddressingType": "DHCP",
                     "ServiceList": "VOIP"}}
edit_ipoe_v4 = {"path": "hbus://wan/editWan",
                "para": {"WanName": "1", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                         "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 1,
                         "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "DHCP",
                         "ServiceList": "INTERNET"}}
edit_ipoe_v6 = {"path": "hbus://wan/editWan",
                "para": {"WanName": "1", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                         "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 2,
                         "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "DHCP",
                         "ServiceList": "INTERNET"}}

edit_ipoe_v46 = {"path": "hbus://wan/editWan",
                 "para": {"WanName": "1", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                          "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 3,
                          "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "DHCP",
                          "ServiceList": "INTERNET"}}

edit_pppoe_v4 = {"path": "hbus://wan/editWan",
                 "para": {"WanName": "2", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 200,
                          "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 1,
                          "NATEnabled": True, "MTU": 1460, "ConnectionType": "PPPoE_Routed", "Username": "test16",
                          "Password": "test16", "ConnectionTrigger": "AlwaysOn", "ServiceList": "INTERNET"}}

edit_pppoe_v6 = {"path": "hbus://wan/editWan",
                 "para": {"WanName": "2", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 200,
                          "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 2,
                          "NATEnabled": True, "MTU": 1460, "ConnectionType": "PPPoE_Routed", "Username": "test16",
                          "Password": "test16", "ConnectionTrigger": "AlwaysOn", "ServiceList": "INTERNET"}}

edit_pppoe_v46 = {"path": "hbus://wan/editWan",
                  "para": {"WanName": "2", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 200,
                           "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 3,
                           "NATEnabled": True, "MTU": 1460, "ConnectionType": "PPPoE_Routed", "Username": "test16",
                           "Password": "test16", "ConnectionTrigger": "AlwaysOn", "ServiceList": "INTERNET"}}

tc_obj = {"path": "hbus://wan/editWan",
          "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 900,
                   "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": True, "IPMode": 1,
                   "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "Static",
                   "ExternalIPAddress": "30.30.30.30", "SubnetMask": "255.255.255.0", "DefaultGateway": "30.30.30.30",
                   "DNSServers": "30.30.30.30", "ServiceList": "INTERNET"}}

add_br_inter = {"path": "hbus://wan/editWan",
                "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "LAN2,LAN3", "VLANMode": 2,
                         "VLANIDMark": 6, "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1500,
                         "ConnectionType": "IP_Bridged", "ServiceList": "INTERNET"}}

add_br_other = {"path": "hbus://wan/editWan",
                "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "LAN3,LAN4", "VLANMode": 2,
                         "VLANIDMark": 6, "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1500,
                         "ConnectionType": "IP_Bridged", "ServiceList": "OTHER"}}

edit_br_other = {"path": "hbus://wan/editWan",
                 "para": {"WanName": "3", "Enable": True, "LanInterface": "LAN3", "VLANMode": 2, "VLANIDMark": 6,
                          "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1500,
                          "ConnectionType": "IP_Bridged", "ServiceList": "OTHER"}}

# get wan name
get_url = "http://192.168.1.1/getHbusData?path=hbus://mdm/getWan&msgType=213&userTagData=1"

# post
add_url = "http://192.168.1.1/setHbusData?path=hbus://mdm/editWan&msgType=213&userTagData=2"

# post wan info
get_info_url = "http://192.168.1.1/setHbusData?path=hbus://mdm/getWan&msgType=213&userTagData=3&waitTimeoutMs=5000&wanIndex=1"

# post del
del_info_url = "http://192.168.1.1/setHbusData?path=hbus://mdm/editWan&msgType=213&userTagData=4&waitTimeoutMs=5000&wanIndex=1"

restoreDefault = "/setHbusData?path=hbus://mdm/RestoreDefault&msgType=201&userTagData=7&waitTimeoutMs=5000"

rest = {"path": "hbus://mdm/RestoreDefault", "para": {}}

login_html = "http://192.168.1.1/lgDevice?userName=CMCCAdmin&responseChallenge=fdf61f287194d3b338612b2705b2a04f"

get_regionUrl = 'http://192.168.1.1/hgsreadme'

telnetUrl = 'http://192.168.1.1/setObjs'
enableTelnet = {"TelnetEnable": True, "TelnetWANEnable": False, "TelnetUserName": "CMCCAdmin",
                "TelnetPassword": "aDm8H%MdA", "fullPath": "InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage."}
telnetTrue = []
telnetTrue.append(enableTelnet)


def json_format(data):
    print(json.dumps(data, sort_keys="True", indent=4, separators=(",", ":")))


class HttpdTest:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""
        }

    def login(self, url):
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            print("\t\tget login info")
            if r.status_code == 200:
                print(r.json()['message'])
        except:
            print('login fail')

    def get_list(self, url):
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            print("\t\tget wan list")
            L = []
            if r.status_code == 200:
                # json_format(r.json())
                # j = r.json()
                # for dict in j:
                #     print('dict:%s, %s' % (j.key(), j.value()))
                for l in r.json()['result']:
                    print('\t\t', l)
                    L.append(l['Index'])
            return L
        except:
            print("error ")

    def get_info(self, url):
        print("\t\tget", url)
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            if r.status_code == 200:
                # print(r.text)
                # json_format(r.json())
                j = r.json()
                # print("\t\tindex = ", j['result'][0]['Index'])
                n = 1
                n = j['result'][0]['Index']
                return n
        except:
            print("error")

    def get_region(self, url=get_regionUrl):
        print("get region")
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            if r.status_code == 200:
                # print(r.text)
                json_format(r.json())
                j = r.json()
                print(j['Region'])
                return 'SMT' in j['Region']
        except Exception as e:
            print(e)

    def post_info(self, url, data):
        try:
            print("\t\tpost", url, data)
            r = requests.post(url, json=data, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # if r.status_code == 200:
            # print('\t\t', r.text)
            # json_format(r.json())
            # print(r.status_code)
        except:
            print("error ")

    def upload_file(self, url, filepath):
        files = {'file': open(filepath, 'rb')}
        r = requests.post(url, files=files)
        print(r.text)


def wanget_set():
    be = HttpdTest()
    print("starting...")

    while 1:
        try:
            L = []
            # get wan name list
            L = be.get_list(get_url)
            print("wan num = ", L, len(L))
            sleep(1)
            # get wan name info
            if len(L) > 0:
                for j in range(20):
                    print("show ", j, end=' ')
                    # for k in L:
                    #     print("show k = ", k, end=' ')
                    # action_1['para']['wanIndex'][0] = k
                    be.post_info(get_info_url, data=action_1)

                # del wan
                for i in L:
                    print("del ...", end='')
                    k = be.get_info(get_url)
                    print(k, end='')
                    action_1['para']['wanIndex'][0] = k
                    be.post_info(del_info_url, data=action_1)
                    sleep(3)
                    be.get_list(get_url)

            # add wan
            obj = [add_int, add_tr69, add_voip, edit_pppoe_v4, edit_ipoe_v4]
            obj_no_voip = [add_int, add_tr69, add_int, edit_pppoe_v46, edit_ipoe_v4]
            obj_tc = [tc_obj]
            for i in obj_tc:
                print("add = ", i, end='')
                # json_format(add_url)
                # json_format(i)
                be.post_info(add_url, data=i)
                sleep(10)
                be.get_list(get_url)
        except Exception as err:
            localtime = time.asctime(time.localtime(time.time()))
            print("out: ", localtime, err)


if __name__ == '__main__':
    be = HttpdTest()
    M = Meminfo(be.get_region())

    be.post_info(telnetUrl, data=telnetTrue)
    print(be.get_region())
    be.login(login_html)

    num = 0
    while 1:
        try:
            L = []
            # get wan name list
            L = be.get_list(get_url)
            print("wan num = ", L, len(L))
            sleep(1)
            # get wan name info
            if len(L) > 0:
                for j in range(20):
                    print("show ", j, end=' ')
                    for k in L:
                        print("show k = ", k, end=' ')
                    action_1['para']['wanIndex'][0] = k
                    be.post_info(get_info_url, data=action_1)

                # del wan
                for i in L:
                    print("del ...", end='')
                    k = be.get_info(get_url)
                    print('\t\t', k, end='')
                    action_1['para']['wanIndex'][0] = k
                    be.post_info(del_info_url, data=action_1)
                    sleep(3)
                    be.get_list(get_url)

            # add wan
            obj = [add_tr69, add_tr69, add_tr69, add_voip, add_voip]
            obj_no_voip = [add_int, add_tr69, add_int, edit_pppoe_v46, edit_ipoe_v4]
            obj_tc = [add_tr69, add_int, add_int, add_br_other, add_voip,
                      edit_ipoe_v4, edit_ipoe_v6, edit_ipoe_v46,
                      edit_pppoe_v4, edit_pppoe_v6, edit_pppoe_v46, edit_br_other]
            for i in obj_tc:
                print("add = ", i, end='')
                # json_format(add_url)
                # json_format(i)
                be.post_info(add_url, data=i)
                sleep(10)
                be.get_list(get_url)

            if 0 == num % 5:
                M.record()
            num += 1


        except Exception as err:
            localtime = time.asctime(time.localtime(time.time()))
            print("out: ", localtime, err)
            # logfile = "wand_test"+
            fo = open("wand_test.log", "w")
            fo.write(localtime)
            fo.write(str(err))
            fo.close()
        finally:
            localtime = time.asctime(time.localtime(time.time()))
            print("out: ", localtime)
