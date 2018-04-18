# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# coding=utf-8
# 
import os
import sys
import shutil

import win32gui
import win32api
import win32con


import telnetlib 
import SendKeys
import unittest, time, re, datetime

import selenium.webdriver.support.ui as UI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from inLine import execute_shell_telnet
from inLine import getCurStartupartition



user_name = 'telnetcom'
pass_wd = 'nE7jA%5m'

login_url = 'http://192.168.1.1/login.html'
mainurl   ='http://192.168.1.1/main.html'
serice_ctrl_url   = 'http://192.168.1.1/scsrvcntr.html'
local_updata_url  = 'http://192.168.1.1/upload.html'
upgrade_file_path = 'D:\linux-file\download\\18.96838GWOVS_ct_e4g1sgw_70ad435d.w'



class autoUpdate(object):
    def loginAcs(self, loginurl=login_url, mainurl = mainurl, username = user_name, passwd = pass_wd):
        print "==login==="
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        time.sleep(1)
        driver.get(loginurl)
        time.sleep()
        
        if mainurl == driver.current_url:
            self.driver = driver
            self.driver.delete_all_cookies()
            return True


if __name__ == '__main__':
    if 1:
        if len(sys.argv) == 2:
            b = autoUpdate(sys.argv[1])
        else:
            b = autoUpdate()
        
        b.loginAcs("80.80.80.40", "http://80.80.80.40/itms/", "admin", "admin")
        