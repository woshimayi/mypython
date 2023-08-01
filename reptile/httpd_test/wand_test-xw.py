#!/usr/bin/env python
# encoding: utf-8
import json
import time
from time import sleep
# import telnetlib

import requests
import sys
import os
from bs4 import BeautifulSoup

# from telnet.telnet_cmcc import Meminfo

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

add_xw_wan = {"path": "hbus://wan/editWan",
              "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2,
                       "VLANIDMark": 1800, "802-1pMark": 0, "IPMode": 2, "MTU": 1500, "ConnectionType": "IP_Routed",
                       "ServiceList": "TR069", "IPv6IPAddressOrigin": "DHCPv6", "IPv6PrefixDelegationEnabled": True,
                       "IPv6PrefixOrigin": "PrefixDelegation", "IPv6DsliteEnable": False}}

add_tc = {"path": "hbus://wan/editWan",
          "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2, "VLANIDMark": 1801,
                   "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": True, "IPMode": 1,
                   "NATEnabled": True, "MTU": 1500, "ConnectionType": "IP_Routed", "AddressingType": "Static",
                   "ExternalIPAddress": "30.30.30.30", "SubnetMask": "255.255.255.0", "DefaultGateway": "30.30.30.30",
                   "DNSServers": "30.30.30.30", "ServiceList": "INTERNET"}}

add_br_inter = {"path": "hbus://wan/editWan",
                "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "LAN2", "VLANMode": 2,
                         "VLANIDMark": 6, "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1500,
                         "ConnectionType": "IP_Bridged", "ServiceList": "INTERNET"}}

add_br_other = {"path": "hbus://wan/editWan",
                "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "LAN1,LAN4", "VLANMode": 2,
                         "VLANIDMark": 6, "802-1pMark": 0, "MulticastVlan": -1, "IPMode": 1, "MTU": 1500,
                         "ConnectionType": "IP_Bridged", "ServiceList": "OTHER"}}

add_int_tc_ipv6 = {"path": "hbus://wan/editWan",
                   "para": {"WanName": "create_new_wan", "Enable": True, "LanInterface": "", "VLANMode": 2,
                            "VLANIDMark": 1801, "802-1pMark": 0, "MulticastVlan": -1, "LanInterface-DHCPEnable": True,
                            "IPMode": 2, "NPTv6Enable": True, "MTU": 1500, "ConnectionType": "IP_Routed",
                            "ServiceList": "INTERNET", "IPv6IPAddressOrigin": "Static", "IPv6IPAddress": "3000::2/64",
                            "IPv6DNSServers": "3000::2", "IPv6PrefixOrigin": "Static", "IPv6Prefix": "2010::2/64",
                            "IPv6DefaultGateway": "3000::2", "IPv6DsliteEnable": False}}

# get wan name
get_url = "http://192.168.1.1/getHbusData?path=hbus://wan/getWan&msgType=213&userTagData=1"

# post
add_url = "http://192.168.1.1/setHbusData?path=hbus://wan/editWan&msgType=213&userTagData=2"

# post wan info
get_info_url = "http://192.168.1.1/setHbusData?path=hbus://wan/getWan&msgType=213&userTagData=3&waitTimeoutMs=5000&wanIndex=1"

# post del
del_info_url = "http://192.168.1.1/setHbusData?path=hbus://wan/editWan&msgType=213&userTagData=4&waitTimeoutMs=5000&wanIndex=1"

restoreDefault = "/setHbusData?path=hbus://mdm/RestoreDefault&msgType=201&userTagData=7&waitTimeoutMs=5000"

restorefactory = "/setHbusData?path=hbus://mdm/RestoreFactory&msgType=201&userTagData=8&waitTimeoutMs=5000"

rest = {"path": "hbus://mdm/RestoreDefault", "para": {}}

factory = {"path": "hbus://mdm/RestoreFactory", "para": {}}

upgrade_url = 'http://192.168.1.1/upgradeImage'

get_regionUrl = 'http://192.168.1.1/hgsreadme'

osgi_start = 'http://192.168.1.1/osgiDebug?action=start'
osgi_stop = 'http://192.168.1.1/osgiDebug?action=stop'

telnetUrl = 'http://192.168.1.1/setObjs'
enableTelnet = {"TelnetEnable": True, "TelnetWANEnable": False, "TelnetUserName": "CMCCAdmin",
                "TelnetPassword": "aDm8H%MdA", "fullPath": "InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage."}
telnetTrue = []
telnetTrue.append(enableTelnet)

getChallengeStr_url = 'http://192.168.1.1//getChallengeStr'
login_url = 'http://192.168.1.1/lgDevice?userName=CMCCAdmin&responseChallenge=424e8cacd1dd80787cdc74b7e3a4fa56'

skip_auth = 'http://192.168.1.1/debug'
skip_auth_data = {"EnableWebDataLog": False, "EnableLogHtmlEle": False, "DisableCommitData": False,
                  "EnableConsolelog": False, "EnableHttpdDebug": False, "EnableSkipAuth": True,
                  "EnableHttpdHbusData": False, "EnableHttpdHbusCmd": False, "EnableDownloadFile": False,
                  "DisablePing": False}


def json_format(data):
    print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))


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

    def get_url(self, url):
        print("\t\tget", url)
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            if r.status_code == 200:
                # print(r.text)
                pass
        except:
            print("error")

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
            else:
                print("post error", r.status_code)
        except Exception as e:
            print("error", e)

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
            else:
                print("post error", r.status_code)
        except Exception as e:
            print(e)

    def post_info(self, url, data):
        try:
            print("\t\tpost", url, data)
            r = requests.post(url, json=data, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                # print('\t\t', r.text)
                # ret = json_format(r.json())
                # print(r.status_code)
                # return ret
                pass
            else:
                print("post error", r.status_code)
        except Exception as e:
            print("post error ", e)

    def upload_file(self, url, filepath):
        files = {'file': open(filepath, 'rb')}
        r = requests.post(url, files=files, stream=True)
        print(r.text)

    def restoredefault(self):
        pass

    def set_config_wan(self):
        pass

    def set_tr069_managment(self):
        pass

    def set_loid_pass(self):
        pass

    def get_wan_info(self):
        pass

    def inform(self):
        pass

    def hello_web(self):
        pass

    def osgi_set(self, status):
        if status:
            get_url(osgi_start)
        else:
            get_url(osgi_stop)

    def isConnect(self, url):
        print("get region")
        try:
            while True:
                r = requests.get(url, headers=self.headers, timeout=20)
                r.encoding = 'utf-8'
                # soup = BeautifulSoup(r.text, "lxml")
                # soup.prettify()
                if r.status_code == 200:
                    return True
                else:
                    print("connect fail")
                sleep(5)
        except Exception as e:
            print(e)

    def login(self):
        self.post_info(skip_auth, skip_auth_data)

    def wanget_set(self):
        print("starting...")

        while 1:
            try:
                L = []
                # get wan name list
                L = self.get_list(get_url)
                print("wan num = ", L, len(L))
                sleep(1)
                # get wan name info
                if len(L) > 0:
                    for j in range(20):
                        print("show ", j, end=' ')
                        # for k in L:
                        #     print("show k = ", k, end=' ')
                        # action_1['para']['wanIndex'][0] = k
                        self.post_info(get_info_url, data=action_1)

                    # del wan
                    for i in L:
                        print("del ...", end='')
                        k = self.get_info(get_url)
                        print(k, end='')
                        action_1['para']['wanIndex'][0] = k
                        self.post_info(del_info_url, data=action_1)
                        sleep(3)
                        self.get_list(get_url)

                # add wan
                obj = [add_int, add_tr69, add_voip, edit_pppoe, edit_ipoe]
                obj_no_voip = [add_int, add_tr69, add_int, edit_pppoe, edit_ipoe]
                obj_xw = [add_xw_wan]
                for i in obj_xw:
                    print("add = ", i, end='')
                    # json_format(add_url)
                    # json_format(i)
                    self.post_info(add_url, data=i)
                    sleep(10)
                    self.get_list(get_url)
            except Exception as err:
                localtime = time.asctime(time.localtime(time.time()))
                print("out: ", localtime, err)
            finally:
                localtime = time.asctime(time.localtime(time.time()))
                print("out: ", localtime)


if __name__ == '__main__':
    be = HttpdTest()
    # M = Meminfo(be.get_region())

    be.login()
    # be.post_info(telnetUrl, data=telnetTrue)
    # print(be.get_region())

    num = 0
    # while 1:
    try:
        # be.upload_file(upgrade_url, r'Z:/build_B560/trunk/images/bcm968782GWV_nand_fs_image_128_puresqubi_V3388.w')
        L = []
        # get wan name list
        L = be.get_list(get_url)
        print("wan num = ", L, len(L))
        sleep(1)
        # get wan name info
        if len(L) > 0:
            # if False:
            # for j in range(20):
            #     print("show ", j, end=' ')
            #     for k in L:
            #         print("show k = ", k, end=' ')
            #     # action_1['para']['wanIndex'][0] = k
            #     ret = be.post_info(get_info_url, data=action_1)
            #     print(ret)

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
        # obj = [add_int, add_tr69, add_voip, edit_pppoe, edit_ipoe]
        # obj_no_voip = [add_int, add_tr69, add_int, edit_pppoe, edit_ipoe]
        # obj_xw = [add_xw_wan]
        # obj_tc = [add_tr69, add_br_other, add_br_inter, add_tc]
        # obj_tc = [add_tr69, add_int, add_br_inter, add_br_other, add_voip, add_tc, add_int, add_voip]
        obj_tc = [add_tr69, add_int]
        for i in obj_tc:
            print("add = ", i, end='')
            # json_format(add_url)
            json_format(i)
            be.post_info(add_url, data=i)
            sleep(10)
            be.get_list(get_url)

        # get_obj = [osgi_stop]
        # for i in get_obj:
        #     be.get_wan_info()

        # if 0 == num%5:
        #     M.record()
        # num += 1
        # time.sleep(60)


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

# if __name__ != '__main__':
#     wanget_set()
