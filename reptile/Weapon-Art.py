#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: Weapon-Art.py
@time: 20/12/29 11:32
@desc: 下载微信公众号 图片
'''

from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys

base_url = 'https://www.dgtle.com/'
url = 'https://m.dgtle.com/ins-detail/1644813'


class BeautifulPicture:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""}

    def mk_dir(self, path):
        self.path = path.strip()
        self.is_exit = os.path.exists(path)
        if not self.is_exit:
            print("创建", path, '文件夹')
            os.makedirs(path)
            print('创建成功')
        else:
            print(path, '文件夹已经存在')
        os.chdir(path)

    def save_img(self, url, name):
        img = requests.get(url)
        print('1', end='')
        f = open(name, 'wb')
        print('2', end='')
        f.write(img.content)
        print(name, '保存成功')
        f.close()

    def save_soap(self, soap, name):
        f = open(name, 'wb')
        f.write(soap)
        print(name, '保存成功')
        f.close()

    def get_pic(self, url):
        r = requests.get(url, headers=self.headers, stream=True)
        r.encoding = 'utf-8'
        # if int(r.headers['content-length']) < TOO_LONG:
        #     content = r.content
        #     print(content)
        # print(r.iter_content())
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()
        # print(soup)

        i = 0
        for jpg_url in soup.find_all('img'):
            i += 1
            time.sleep(0.5)
            print('0', jpg_url)

            if jpg_url.get('data-src') is not None and 'http' in jpg_url.get('data-src'):
                tmp_url = jpg_url.get('data-src')
            elif jpg_url.get('src') is not None and 'http' in jpg_url.get('src'):
                tmp_url = jpg_url.get('src')
            else:
                continue

            print('1', tmp_url)
            picture_name = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + str(i) + '.jpg'
            print(picture_name, end='')
            self.save_img(tmp_url, picture_name)

    def get_next_url(self):
        for jpg_url in soup.find_all('a'):
            if 'http' in jpg_url['href']:
                print(jpg_url['href'])
                # print('成功')
            else:
                print(base_url + jpg_url['href'])


if __name__ == '__main__':
    # if len(sys.argv) < 3:
    #     print("argc less three")
    be = BeautifulPicture()
    path = r'./get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    be.mk_dir(path)
    # url = r'https://mp.weixin.qq.com/s/tOJBsu1F8YQAn7e1X1wJfA'
    url = r'https://mp.weixin.qq.com/s/B5ctgRy6G9CyqudYsEyzXw'
    
    # url = sys.argv[1]
    print(url)
    be.get_pic(url)
