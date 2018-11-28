#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:17:25 2018

@author: zs
"""

from selenium import webdriver
import os

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.quit()