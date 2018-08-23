#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:17:25 2018

@author: zs
"""

from selenium import webdriver
import os

driver = webdriver.Chrome(os.path.expanduser('/usr/bin/chromedriver'))

driver.get("http://www.google.com")

driver.quit()