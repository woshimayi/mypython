'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: wifi_connect_bssid.py
@time: 2025/02/28 14:17
@desc: 
'''


import pywifi
from pywifi import const
import time

def connect_wifi(ssid, bssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)

    profile = pywifi.Profile()
    profile.ssid = ssid
    # profile.auth = const.AUTH_ALG_WPA2PSK
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    profile.bssid = bssid

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(10)

    if iface.status() == const.IFACE_CONNECTED:
        print("Wi-Fi 连接成功！")
    else:
        print("Wi-Fi 连接失败！")

# 使用示例
ssid = "CMCC-GD252C01-5G"
bssid = "24:8B:E0:E5:37:78"
password = "12345678"

connect_wifi(ssid, bssid, password)


if __name__ == '__main__':
    print('Hello world')
