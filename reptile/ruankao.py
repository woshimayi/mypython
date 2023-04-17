#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: ruankao.py
@time: 23/3/20 15:31
@desc: 软考报名时间
'''



from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys

url = 'https://bm.ruankao.org.cn/sign/welcome'

class BeautifulPicture:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""}

    def get_pic(self, url):
        r = requests.get(url, headers=self.headers, stream=True)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()
        i = 0
        flag = False
        for jpg_urls in soup.find_all(name='div'):
            i += 1
            if "col1" in jpg_urls.get("class"):
                if '上海' in jpg_urls.get_text():
                    print(jpg_urls.get_text(), end=' ')
                    flag = True
            elif flag and "timeW" in jpg_urls.get("class"):
                print(jpg_urls.get_text())
                if flag:
                    break



if __name__ == '__main__':
    be = BeautifulPicture()
    be.get_pic(url)
    input('按任意键继续：..........')
    print('hello world')
