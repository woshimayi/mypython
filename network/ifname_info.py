#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: ifname_info.py
@time: 2022/10/9 9:50
@desc:
'''
import pprint
import subprocess
import re


# 执行windows命令
import netifaces
import scapy
from scapy.all import *


def exec_command(commands) -> list:
    """执行windows命令"""
    if not commands:
        return list()
    # 子进程的标准输出设置为管道对象
    if isinstance(commands, str):
        commands = [commands]
    return_list = []
    for i in commands:
        p = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        p.wait()
        res = "".join(p.stdout.readlines())
        return_list.append(res)
    return return_list


def get_net_card():
    """
    功能：通过ipconfig返回的文本解析网卡名字、ip、掩码、网关等信息
    注释：简单做了注释
    测试：在window10 专业版测试通过（可以检测到以太网两个（包含手机、网线）、wifi一个）
    测试反馈：如果使用发现其余问题可以反馈到 sunnylishaoxu@163.com,非常感谢
    说明一：
       默认网关. . . . . . . . . . . . . : fe80::10b1:1865:86e8:ad10%41
                                           172.20.10.1
    """
    net_card_data = list()
    res = exec_command("ipconfig")
    temp_dict = dict(flag=True)
    gateway_error = False
    for x in res[0].splitlines():
        # 匹配IP正则
        pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        # 测试发现有的网关会默认在下一行，情况见说明一，所以这边检查到默认网关，发现没有匹配到，则从下一行找
        if gateway_error:
            print('zzz', pattern.search(x))
            temp_dict['gateway1'] = pattern.search(x).group()
            gateway_error = False
            print("当前网卡 %s 获取第二行网关信息 %s" % (temp_dict['card_name'], temp_dict['gateway1']))
            continue
        # 如果发现新的适配器，则重置上一个网卡是否可用的状态
        if "适配器" in x:
            temp_dict = dict(flag=True)
            temp_dict['card_name'] = x.split(" ", 1)[1][:-1]
            print("当前网卡 %s" % (temp_dict['card_name']))
            continue
        if "IPv4 地址" in x:
            temp_dict['ip'] = pattern.search(x).group()
            print("当前网卡 %s 获取IP信息 %s" % (temp_dict['card_name'], temp_dict['ip']))
            continue
        elif "子网掩码" in x:
            temp_dict['mask'] = pattern.search(x).group()
            print("当前网卡 %s 获取子网掩码信息 %s" % (temp_dict['card_name'], temp_dict['mask']))
            continue
        # 测试发现有的网关会默认在下一行，情况见说明一，所以这边做了异常处理
        elif "默认网关" in x:
            try:
                temp_dict['gateway1'] = pattern.search(x).group()
                print("当前网卡 %s 获取默认网关信息 %s" % (temp_dict['card_name'], temp_dict['gateway1']))
            except:
                gateway_error = True
                print("当前网卡 %s 解析当前行默认网关信息错误" % (temp_dict['card_name']))

            # 如果检查到网关，代表当前适配器信息已经获取完毕 重置网关状态与适配器信息字典
            if temp_dict.get("gateway1"):
                net_card_data.append(temp_dict)
                print("当前网卡 %s 当前适配器信息获取完毕 %s \n\n" % (temp_dict['card_name'], temp_dict))

                temp_dict = dict(flag=True)
                continue
        # 发现媒体已断开则更改当前适配器状态
        elif "媒体已断开" in x:
            print("当前网卡 %s 已断开 跳过\n\n" % (temp_dict['card_name']))
            temp_dict['flag'] = False
            continue
        # 判断媒体状态正常，IP、子网掩码、网关都正常后，保持起来
        if temp_dict.get("flag") and temp_dict.get("ip") and temp_dict.get("mask") and temp_dict.get("gateway1"):
            print("当前网卡 %s 当前适配器信息获取完毕 %s \n\n" % (temp_dict['card_name'], temp_dict))
            net_card_data.append(temp_dict)
            # 重置网关状态与适配器信息字典
            temp_dict = dict(flag=True)
            continue
    for i in net_card_data:
        print("%s：%s" % (i.get("card_name"), i))
    return net_card_data


if __name__ == '__main__':
    # ifaces.show()
    ifnames = str(ifaces).splitlines(False)
    for ifname in ifnames:
        if_arg = ifname.split()
        # print(if_arg)
        if len(if_arg) > 6:
            print(dev_from_index(if_arg[1]), if_arg[-1])
    # print(get_if_list())
    # print(get_if_addr('lan'))
    # print(get_if_hwaddr('lan'))
    print(get_working_if())
    print('hello world')
