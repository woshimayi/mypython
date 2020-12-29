#coding:utf-8
import webbrowser as web #对导入的库进行重命名
import os
import time


def use_chrome_open_url(url):
    browser_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    web.register('chrome', None,web.BackgroundBrowser(browser_path))
    web.get('chrome').open_new_tab(url)
    print('use_chrome_open_url open url ending ....')