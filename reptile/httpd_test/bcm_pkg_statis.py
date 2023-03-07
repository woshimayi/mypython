#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: bcm_pkg_statis.py
@time: 23/2/24 14:40
@desc:
'''
import requests
import json

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
edit_ipoe = {"path": "hbus://wan/editWan",
             "para": {"WanName": "1", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 6,
                      "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 1,
                      "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "DHCP",
                      "ServiceList": "INTERNET"}}
edit_pppoe = {"path": "hbus://wan/editWan",
              "para": {"WanName": "2", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 200,
                       "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": 1, "IPMode": 1,
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
get_url = "http://192.168.1.1/getHbusData?path=hbus://wan/getWan&msgType=213&userTagData=1"

# post
add_url = "http://192.168.1.1/setHbusData?path=hbus://wan/editWan&msgType=213&userTagData=2"

# post wan info
get_info_url = "http://192.168.1.1/setHbusData?path=hbus://wan/getWan&msgType=213&userTagData=3&waitTimeoutMs=5000&wanIndex=1"

# post del
del_info_url = "http://192.168.1.1/setHbusData?path=hbus://wan/editWan&msgType=213&userTagData=4&waitTimeoutMs=5000&wanIndex=1"

restoreDefault = "/setHbusData?path=hbus://mdm/RestoreDefault&msgType=201&userTagData=7&waitTimeoutMs=5000"

rest = {"path": "hbus://mdm/RestoreDefault", "para": {}}

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
            if r.status_code == 200:
                # print('\t\t', r.text)
                # json_format(r.json())
                print(r.status_code)
        except:
            print("error ")

    def upload_file(self, url, filepath):
        files = {'file': open(filepath, 'rb')}
        r = requests.post(url, files=files)
        print(r.text)


class Pkg(object):
    """docstring for Pkg"""

    def __init__(self, arg):
        super(Pkg, self).__init__()
        self.arg = arg

        self.bs_z = "bs /b/z"
        self.port_wan0 = "bs /b/e port/index=wan0"
        self.ethswctl = "ethswctl -c mibdump -a"


if __name__ == '__main__':
    be = HttpdTest()
    be.post_info(telnetUrl, data=telnetTrue)

    M = Meminfo(be.get_region())
    M.record()

    print('hello world')

