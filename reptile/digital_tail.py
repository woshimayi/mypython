#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: digital-tail.py
@time:
@desc: 下载数字尾巴 微信公众号 bing首页 等一些图片保存到文件夹中
'''
import argparse

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
        if url is not None and 'http' in url:
            img = requests.get(url, headers=self.headers, stream=True)
            # print('img size: ', img.content)
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
        # print('aaa', len(soup.find_all('img')))
        for jpg_url in soup.find_all('img'):
            i += 1

            # print(jpg_url)
            time.sleep(0.5)

            if jpg_url.get('data-original') is not None and 'http' in jpg_url.get('data-original'):
                tmp_url = jpg_url.get('data-original')
            elif jpg_url.get('src') is not None and 'http' in jpg_url.get('src'):
                tmp_url = jpg_url.get('src')
            elif jpg_url.get('data-src') is not None and 'http' in jpg_url.get('data-src'):
                tmp_url = jpg_url.get('data-src')
            else:
                continue

            # print('1', tmp_url)
            picture_name = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + str(i) + '.jpg'
            print(picture_name, end='')
            self.save_img(tmp_url, picture_name)

        os.chdir('../')

    def get_bing(self, url):
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
        # print('aaa', soup.find_all('img'))
        for jpg_url in soup.find_all('a'):
            i += 1

            print(jpg_url)
            time.sleep(0.5)

        # os.chdir('../')

    def get_next_url(self):

        for jpg_url in soup.find_all('a'):
            if 'http' in jpg_url['href']:
                print(jpg_url['href'])
                # print('成功')
            else:
                print(base_url + jpg_url['href'])


if __name__ == '__main__':

    if 1:
        parser= argparse.ArgumentParser()
        # group = parser.add_mutually_exclusive_group()

        parser.add_argument("-v", "--version", action="store_true", default=0, help="otuput version info")
        parser.add_argument("url", type=str, nargs="?", help="input the url")
        # parser.add_argument("url", type=str, help="input the url")
        parser.add_argument("-o", "--output", help="otuput specify dirctory")
        parser.add_argument("-f", "--file", help="Get the url in file")
        parser.add_argument("-b", "--bing", action="store_true", help="Get the url in file")

        # 添加到参数列表中
        args = parser.parse_args()


        if args.output:
            directory = args.output
        elif args.file:
            file = args.file
        else:
            pass

        print(args)

        if args.url is not None:
            print(args.url)
            url = args.url
        else:
            # 打开命令直接获取剪贴板内容，如果是url，直接下载
            import clipboard
            url = clipboard.paste()

            print(url)
            # if 'http' in url and 'html' in url:
            if 'http' in url:
                # be.get_pic(url)
                pass
            else:
                print('no html')

        if args.output is not None:
            os.chdir(directory)
        print(os.getcwd())

    if 'bing' in url and 'http' in url:
        print('bing picture')
        path = r'get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        be = BeautifulPicture()
        be.mk_dir(path)
        be.get_bing(url)
    elif args.bing:
        # 获取bing 首页壁纸
        url = r'https://api.dujin.org/bing/1920.php'

        be = BeautifulPicture()
        if os.path.isdir("bing-img") == False:
            be.mk_dir('bing-img')
        else:
            os.chdir("bing-img")
        jpg = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + '_bing-img.jpg'
        be.save_img(url, jpg)
    else:
        path = r'get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        be = BeautifulPicture()
        be.mk_dir(path)

        # mobil url to pc url
        if "ins-detail" in url:
            index = url.split('/')[-1]
            print(index)
            url = base_url + 'article-' + \
                      url.split('/')[-1] + '-1.html'
            print(url)
        be.get_pic(url)

    # remove empty dir
    if 0 == len(os.listdir(path)):
        os.rmdir(path)


