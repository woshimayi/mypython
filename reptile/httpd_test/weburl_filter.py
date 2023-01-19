#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: weburl_filter.py
@time: 22/12/22 16:03
@desc:
'''
from time import sleep

import requests
from bs4 import BeautifulSoup


class HttpdTest:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
        }

    def get_list(self, url):
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "lxml")
            soup.prettify()
            if r.status_code == 200:
                # print(soup)
                print("200 OK")
            else:
                print(r.status_code)
        except:
            print("error ")


if __name__ == '__main__':
    b = HttpdTest()
    url = "https://www.baidu.com"


    while True:
        b.get_list(url)
        sleep(2)



    print('hello world')
