#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:26:22 2018

@author: zs
"""

from selenium import webdriver
import time 
import threading


login_url = 'http://192.168.0.2/login.html'
main_url  ='http://192.168.0.2/main.html'
user_name = 'root'
pass_wd   = 'root'

url_list = ['window.open("http://192.168.0.3/login.html")'
			,'window.open("http://192.168.0.4/login.html")'
			,'window.open("http://192.168.0.5/login.html")'
			,'window.open("http://192.168.0.6/login.html")'
			,'window.open("http://192.168.0.7/login.html")'
			,'window.open("http://192.168.0.8/login.html")'
			,'window.open("http://192.168.0.9/login.html")'
			,'window.open("http://192.168.0.10/login.html")'
			,'window.open("http://192.168.0.11/login.html")']

browser = webdriver.Chrome()

browser.get(login_url)

def upgrade():
	browser.find_element_by_id('LOGIO_TEXT_UserName').clear()  #清理 
	browser.find_element_by_id('LOGIO_TEXT_UserName').send_keys(user_name)
	browser.find_element_by_id("LOGIO_PWD_Password").clear()   #清除对象的内容
	browser.find_element_by_id("LOGIO_PWD_Password").send_keys(pass_wd)	 #在对象上模拟按键键入
	browser.find_element_by_id("BTN_Login").click()	  #点击
	time.sleep(1)
	browser.find_element_by_id("treeDemo_33_span").click()	 
	browser.find_element_by_id("treeDemo_36_span").click()	 
	browser.switch_to_frame('MainFrameid')
	browser.find_element_by_xpath('//*[@id="concentfile"]').send_keys('/home/zs/Music/EPON_MTK004_0001_JISHIHUITONG_ONU_V1.2_R1B01Df62034b8_934adc10.squashfs.upf')
	browser.find_element_by_id("upBtn").click()

for i in url_list:
	print(i)
	browser.execute_script(i)
	time.sleep(1)

handles = browser.window_handles
browser.switch_to_window(handles[0])
browser.switch_to_window(handles[1])
browser.switch_to_window(handles[2])
browser.switch_to_window(handles[3])
browser.switch_to_window(handles[4])
browser.switch_to_window(handles[5])
browser.switch_to_window(handles[6])
browser.switch_to_window(handles[7])
browser.switch_to_window(handles[8])
browser.switch_to_window(handles[9])

# j=0
# for j in range(10):
# 	print(j)
# 	upgrade()









# time.sleep(1)

# js='window.open("http://192.168.0.3");'
# browser.execute_script(js)
# time.sleep(1)

# js='window.open("http://192.168.0.4");'
# browser.execute_script(js)
# time.sleep(1)

# js='window.open("http://192.168.0.5");'
# browser.execute_script(js)
# time.sleep(1)

# handles = browser.window_handles
# browser.switch_to_window(handles[0])