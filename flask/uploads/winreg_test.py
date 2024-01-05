# encoding:utf-8
from winreg import *
import sys

# 1.连接注册表根键，以HKEY_LOCAL_MACHINE为例
regRoot = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

subDir = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
# 2.获取指定目录下所有键的控制(可用于遍历)
keyHandle = OpenKey(regRoot, subDir)
count = QueryInfoKey(keyHandle)[0] # 获取该目录下所有键的个数(0-下属键个数;1-当前键值个数)
for i in range(count):
    # 3.穷举每个键，获取键名
    subKeyName = EnumKey(keyHandle, i)
    subDir_2 = r'%s\%s' % (subDir, subKeyName)
    # 4.根据获取的键名拼接之前的路径作为参数，获取当前键下所属键的控制
    keyHandle_2 = OpenKey(regRoot, subDir_2)
    count2 = QueryInfoKey(keyHandle_2)[1]
    for j in range(count2):
        # 5.穷举每个键，获取键名、键值以及数据类型
        name, value, type = EnumValue(keyHandle_2, j)
        if('ProfileImagePath' in name and 'Users' in value):
            print(value)
    CloseKey(keyHandle_2) # 读写操作结束后关闭键

CloseKey(keyHandle)
CloseKey(regRoot)