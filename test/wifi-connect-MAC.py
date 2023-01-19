from time import sleep
import sys
import pywifi
from pywifi import const

def wifi_connect(ssid,password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # 取一个无线网卡
    iface.remove_all_network_profiles()
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN  # 需要秘密
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
    profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = password
    sleep(3)
    profile = iface.add_network_profile(profile)
    iface.connect(profile)
    sleep(3)  # 程序休眠时间3秒；如果没有此句，则会打印连接失败，因为它需要一定的检测时间
    if iface.status() == const.IFACE_CONNECTED:
        print("连接成功！！！")
        return 1
    else:
        print("连接失败！！！")
        return 0


if __name__=='__main__':
    for i in range(1,5000):
        #将日志输出到指定路径
        f = open('E://ProjectTest//test.log', 'a+')
        sys.stdout = f
        print("第%d次连接" % i)
        sleep(5)
        wifi_connect('CMCC-5G-hgtest14','12345678')#填写连接的SSID，和密码，这里加密方式用的WPA2-PSK，其它加密方式可以修改配置文件

