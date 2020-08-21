#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: digi-js.py.py
@time: 2020/8/19 10:12
@desc:
'''

# -*- coding: utf-8 -*-
import bs4
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# 利用PhantomJS加载网页
browser = webdriver.PhantomJS()
browser.set_page_load_timeout(5)  # 最大等待时间为30s
# 当加载时间超过30秒后，自动停止加载该页面
try:
    browser.get('http://comic.kukudm.com/comiclist/43/395/4.htm')
except TimeoutException:
    browser.execute_script('window.stop()')
source = browser.page_source  # 获取网页源代码
browser.quit()
# 解析网页，获取下载图片的网址
soup = BeautifulSoup(source, 'lxml')
image = soup.find('img')
url = image.get('src')
# 下载图片
urllib.request.urlretrieve(url, r"G:\\爬虫图片\浪客剑心.jpg")
print("Download picture successfully!")
