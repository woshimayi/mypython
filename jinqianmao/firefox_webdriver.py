#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:05:14 2018

@author: zs
"""

#-*- coding:utf-8 -*-
from selenium import webdriver
#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys(u'MoonBreeze的博客')
driver.find_element_by_id('su').click()