'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: wifi_connect_bssid.py
@time: 2025/02/28 14:17
@desc: 连接指定的wifi bssid
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
ssid = "CMCC-GD252C01"
# bssid = "24:8b:e0:e5:33:78"
bssid = "a4:a5:28:23:22:29"
password = "12345678"

L = ["a4:a5:28:23:22:29", "24:8b:e0:e5:2d:81"]

if False:
    while True:
        for b in L:
            connect_wifi(ssid, b, password)
            time.sleep(15)
        time.sleep(15)
else:
    connect_wifi(ssid, bssid, password)



if __name__ == '__main__':
    print('Hello world')
