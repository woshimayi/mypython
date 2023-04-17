#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: request-html_test.py
@time: 23/1/20 10:53
@desc:
'''
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()

# r = session.get('https://m.dgtle.com/ins-detail/1850884', verify=False)
# r.html.render()  # 首次使用，自动下载chromium
# b = r.html.
# d = r.html.find(".http")
# print(r.html.links)
# print(r.html.absolute_links)
# print(d.text)
# soup = BeautifulSoup(b, "lxml")
# soup.prettify()
# print(soup)
# print('aaa', soup.find_all('img'))
# print('aaa', len(soup.find_all('img')))

from requests_html import HTMLSession
session = HTMLSession()

# r = session.get('https://m.dgtle.com/ins-detail/1850884', verify=False)
# r.html.render()  # 首次使用，自动下载chromium
# print(r.html.html)
# d = r.html.find("#profile_block", first=True)
# soup = BeautifulSoup(r.html.html, "lxml")
# soup.prettify()
# print(soup)
# print('aaa', soup.find_all('img'))
# print('aaa', len(soup.find_all('img')))
# urls = soup.find_all('img')
# for url in urls:
#     print(url)
# print(d.text)

r = session.get('https://m.dgtle.com/ins-detail/1850884')

# 获取页面上的所有链接
all_links = r.html.links
print(all_links)

# 绝对路径链接
all_absolute_links = r.html.absolute_links
print(all_absolute_links)


if __name__ == '__main__':
    print('hello world')
