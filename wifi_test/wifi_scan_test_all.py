'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: wifi_scan_test_all.py
@time: 2025/05/15 11:06
@desc: 
'''

import pywifi
from pywifi import const
import time


def scan_wifi():
    wifi = pywifi.PyWiFi()

    # 获取无线网卡接口
    try:
        ifaces = wifi.interfaces()
        if not ifaces:
            print("没有找到无线网卡接口！")
            return None
        interface = ifaces[0]  # 假设第一个接口是我们要使用的
        print(f"使用的无线网卡接口: {interface.name()}")
    except pywifi.PyWiFiError as e:
        print(f"获取无线接口时发生错误: {e}")
        return None

    # 开始扫描
    print("开始扫描周围 Wi-Fi 网络...")
    interface.scan()
    time.sleep(5)  # 等待扫描完成 (根据环境调整等待时间)

    scan_results = interface.scan_results()
    if not scan_results:
        print("没有扫描到任何 Wi-Fi 网络。")
        return []

    wifi_list = []
    for result in scan_results:
        ssid = result.ssid.encode('latin-1').decode('utf-8', 'ignore') if result.ssid else "隐藏 SSID"
        bssid = result.bssid if result.bssid else "N/A"
        freq = result.freq if result.freq else "N/A"
        signal = result.signal if result.signal is not None else "N/A"
        # mode = get_wifi_standard(result.)
        mode = ""
        channel = calculate_channel(freq) if freq != "N/A" else "N/A"

        wifi_info = {
            "SSID": ssid,
            "BSSID": bssid,
            "频率": freq,
            "信道": channel,
            "强度": signal,
            "标准": mode
        }
        wifi_list.append(wifi_info)

    return wifi_list


def get_wifi_standard(mode_code):
    """根据模式代码获取 Wi-Fi 标准"""
    if mode_code == const.AUTH_ALG_OPEN:
        return "OPEN"
    elif mode_code == const.AUTH_ALG_SHARED:
        return "SHARED"
    elif mode_code == const.AUTH_ALG_LEAP:
        return "LEAP"
    elif mode_code == const.WPA_AUTH_KEY_MGMT:
        return "WPA"
    elif mode_code == const.RSN_AUTH_KEY_MGMT:
        return "WPA2"
    elif mode_code == const.WPA2_AUTH_KEY_MGMT:
        return "WPA2"  # 某些情况下可能返回这个
    elif mode_code == const.WPA2_PSK:
        return "WPA2-PSK"
    elif mode_code == const.WPA_PSK:
        return "WPA-PSK"
    elif mode_code == const.WPA3_SAE:
        return "WPA3-SAE"
    else:
        return "未知"


def calculate_channel(frequency):
    """根据频率计算 Wi-Fi 信道 (近似)"""
    if 2400 <= frequency <= 2500:
        # 2.4 GHz band
        return round((frequency - 2412) / 5 + 1)
    elif 5000 <= frequency <= 6000:
        # 5 GHz band (simplified)
        return round((frequency - 5000) / 5 + 36)  # 这是一个非常简化的近似
    else:
        return "未知"


if __name__ == "__main__":
    wifi_networks = scan_wifi()
    if wifi_networks:
        print("\n扫描到的 Wi-Fi 网络:")
        for network in wifi_networks:
            print(f"  SSID: {network['SSID']}", end="")
            print(f"  BSSID: {network['BSSID']}", end="")
            print(f"  频率: {network['频率']} MHz", end="")
            print(f"  信道: {network['信道']}", end="")
            print(f"  强度: {network['强度']} dBm", end="")
            print(f"  标准: {network['标准']}", end="")
            print("-" * 20)
