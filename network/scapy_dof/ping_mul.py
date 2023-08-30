'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: ping_mul.py
@time: 23/6/30 15:35
@desc:
'''

import logging
import ipaddress
import multiprocessing
from random import randint
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def ping(host, queue=None):
    """
    ping一个主机
    :param host: 主机地址
    :param queue: 成功时将地址放入该队列
    :return:
    """
    print("Testing：", host)
    id_ip = randint(1, 65535)
    id_ping = randint(1, 65535)
    seq_ping = randint(1, 65535)
    pkt = IP(dst=str(host), ttl=1, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b"I'm a ping packet "  # 构造ping包
    reply = sr1(pkt, timeout=2, verbose=False)  # 接收一个回复包
    if reply:
        print(host, "success")
        if queue is not None:
            queue.put(host)


def scan(network, sacnFunc, maxPool=0, maxQueue=0):
    """
    对一个局域网进行扫描
    :param network: 扫描一个局域网
    :param sacnFunc: 用到的扫描函数
    :param maxPool: 最大进程数，如果不指定的话为本机CPU数量
    :param maxQueue: 队列最大数量
    :return: 返回
    """
    queue = multiprocessing.Manager().Queue(maxQueue)
    net = ipaddress.ip_network(network)  # 将网段解析为所有地址
    pool = multiprocessing.Pool(maxPool if maxPool else multiprocessing.cpu_count())
    for ip in net:
        pool.apply(sacnFunc, (ip, queue))

    pool.close()
    pool.join()
    successful_ip_list = []
    while not queue.empty():
        host = queue.get()
        successful_ip_list.append(host)

    return sorted(successful_ip_list)


if __name__ == '__main__':
    import time

    start = time.time()
    print("Start scanning ...")
    active_ip = scan("192.168.1.0/24", ping)
    print("Scan complete!")
    print("The hosts successfully scanned are:")
    for i, ip in enumerate(active_ip):
        print("{}: {}".format(i, ip))
    print("\nA total of {} addresses were successful!\n".format(len(active_ip)))
    end = time.time()
    print("This scan takes a total of {} seconds.".format(end - start))
