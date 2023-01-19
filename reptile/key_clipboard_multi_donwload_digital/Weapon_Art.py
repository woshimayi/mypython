#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
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
import codecs

from Data_storage.json.json_dof import json_Dof

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
        os.chdir('../')

    def get_next_url(self, url):
        r = requests.get(url, headers=self.headers, stream=True)
        # r.encoding = 'utf-8'
        r.encoding = 'GBK'
        # if int(r.headers['content-length']) < TOO_LONG:
        #     content = r.content
        #     print(content)
        # print(r.iter_content())
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()
        
        
        url_L = []
        for jpg_url in soup.find_all('a'):
            if jpg_url.get('href') is not None and '.html' in jpg_url.get('href') and 'news' in jpg_url.get('href'):
                if jpg_url.get('title') is None:
                    continue
                print(jpg_url['href'])
                url_L.append({"url": base_url + jpg_url.get('href'), "title": jpg_url.get('title')})
                
        return url_L

if __name__ == '__main__':
    # if len(sys.argv) < 3:
    #     print("argc less three")
    be = BeautifulPicture()
    # path = r'./get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # be.mk_dir(path)
    # url = r'https://mp.weixin.qq.com/s/tOJBsu1F8YQAn7e1X1wJfA'
    # url = r'https://mp.weixin.qq.com/s?__biz=MzI1ODUzNjQ1Mw==&mid=2247544433&idx=1&sn=90c06690e582d4859d5767113ab329b2&chksm=ea04cb1bdd73420d586188c5d33ada893a9643e94eeb6bf129f0b6250ffd659f8242b624ff6f&scene=132#wechat_redirect'
    
    base_url = 'http://www.biketo.com'
    url = 'http://www.biketo.com/beauty/'
    # url = 'http://www.biketo.com/app.php?m=info&a=getNewsList&type=column&id=33&page=6'
    

    j = json_Dof('bickcle.json')
    if not os.access('bickcle.json', os.F_OK):
        obj = be.get_next_url(url)
        print(obj)
        j.write(obj)
    else:
        r = j.read()
    
        for i in range(len(r)):
            print('---', r[i]['url'], r[i]['title'])
            if r[i]['title'] is None:
                path = r'./get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            else:
                path = r[i]['title']
            be.mk_dir(path)
            be.get_pic(r[i]['url'])
    
    # url = sys.argv[1]
    # print(url)
    # be.get_pic(url)
