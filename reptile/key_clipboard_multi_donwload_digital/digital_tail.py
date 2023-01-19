#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: digital-tail.py
@time:
@desc: 下载数字尾巴图片
'''


import clipboard
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
        if len(img.content) > 30000:
            f = open(name, 'wb')
            f.write(img.content)
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

            # print(jpg_url['src'])
            time.sleep(0.5)
            if 'http' in jpg_url['src']:
                # print(jpg_url['alt'])
                print(str(time.strftime("%Y%m%d%H%M%S",
                                        time.localtime())) + str(i) + '.jpg')
                self.save_img(
                    jpg_url['src'], str(
                        time.strftime(
                            "%Y%m%d%H%M%S", time.localtime())) + str(i) + '.jpg')

    def get_next_url(self):

        for jpg_url in soup.find_all('a'):
            if 'http' in jpg_url['href']:
                print(jpg_url['href'])
                # print('成功')
            else:
                print(base_url + jpg_url['href'])


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("argc less three")
    be = BeautifulPicture()
    os.chdir(r'C:/Users/zs-work/Pictures/')
    print(os.getcwd())

    path = r'E:/相册/上海2020/get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    be.mk_dir(path)

    # url = r'https://opser.wap.dgtle.com/#/interestTopicDetails/1646384'
    # index = url.split('/')[-1]
    # url = base_url+''+'inst-'+index+'-1.html'
    print(sys.argv)
    be.get_pic(sys.argv[1])


    # url  = sys.argv[1]
    url = clipboard.paste()
    print(url)
    if 'http' in url and 'html' in url:
        be.get_pic(url)
    else:
        print('no html')
