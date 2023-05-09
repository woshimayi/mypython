#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: dns_test.py
@time: 23/5/5 15:10
@desc: 多线程 dns 解析 压力测试
'''
import os
import threading
import time

import dns.resolver
import requests

file_dns = 'dsnlist.txt'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    'authorization': ""}


def http_request(domain):
    url = 'http://' + domain
    r = requests.get(url, headers=headers, stream=True)
    print(r.status_code)


def dns_query(domain):
    # 获取解析对象
    query_object = dns.resolver.resolve(qname=domain, rdtype='A')  # 指定查询记录为A
    print('查询对象：{}'.format(query_object))

    print('*' * 100)

    # 查看response对象
    response_object = query_object.response
    # print('应答对象：{}'.format(response_object))

    print('*' * 100)

    # 查询answer对象
    answer_object = response_object.answer
    print('解析对象：{}'.format(answer_object))

    print('*' * 100)

    # 查看解析条目对象
    # answer_object = response_object.answer
    # for query_item in answer_object:
    #     print('查询条目：{}'.format(query_item))

    # print('*' * 100)

    # 解析后的记录条目
    # query_item = response_object.answer[0]
    # # print(query_item)
    # for item in query_item:
    #     print('解析记录：{}'.format(item))

    # print('*' * 100)


def test():
    while True:
        try:
            os.system('ipconfig /flushdns')
            # 没有文件 创建文件
            # if not os.access(file_dns, os.F_OK):
            #     with open(file_dns, 'w') as f:
            #         f.close()

            # 获取文件内容
            with open(file_dns, 'rt', newline="") as f:
                lines = f.readlines()
                f.close()
                print('1', lines)

            for line in lines:
                print('2', line.splitlines()[0])
                # dns_query(line.splitlines()[0])
                http_request(line.splitlines()[0])
        except Exception as e:
            print(e)


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if __name__ == '__main__':

    if not os.access(file_dns, os.F_OK):
        with open(file_dns, 'w') as f:
            f.close()
        exit()

    # 2:在线程池中创建几个线程
    pool = ThreadPoolExecutor(10)  # 创建10个线程

    # 3:在线程池中发任务
    for i in range(100):
        pool.submit(test(), i)

    # 4:等待线程池把任务都执行完毕
    pool.shutdown()

    print('hello world')
