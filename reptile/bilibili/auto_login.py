'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: auto_login.py
@time: 23/9/22 17:27
@desc:  自动登录 bilibili 网站
'''

from selenium import webdriver
import time
import json


class AutoLogin(object):
    """docstring for AutoLogin"""

    def __init__(self):
        super(AutoLogin).__init__()

        options = webdriver.EdgeOptions()
        # options.add_argument('--disable-infobars')
        # options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
        options.page_load_strategy = 'eager'
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Edge(options=options)

    def getCookie(self):
        self.driver.get('https://www.bilibili.com/')

        '''
        打开网页后直接登录
        手动登录完成后在命令行内按回车，因为我用input阻塞了
        等提示进程已结束，退出代码，可以看到同级目录下多出一个名为 jsoncookie.json的文件。里面存的是cookie
        '''

        self.driver.implicitly_wait(10)

        input()
        dictcookie = self.driver.get_cookies()
        print('dictcookie:', dictcookie)

        jsoncookie = json.dumps(dictcookie)
        print('jsoncookie:', jsoncookie)
        with open('jsoncookie.json', 'w') as f:
            f.write(jsoncookie)
        self.driver.close()

    def login(self):
        self.driver.get('https://www.bilibili.com/')
        # 删除本次打开网页时的所有cookie
        self.driver.delete_all_cookies()
        with open('jsoncookie.json', 'r') as f:
            ListCookies = json.loads(f.read())
        # 将jsoncookie.json里的cookie写入本次打开的浏览器中。
        for cookie in ListCookies:
            self.driver.add_cookie({
                'domain': '.bilibili.com',
                'name': cookie['name'],
                'value': cookie['value'],
                'path': '/',
                'expires': None,
                'httponly': False,
            })
            time.sleep(1)
            self.driver.get('https://www.bilibili.com/')


if __name__ == '__main__':
    print('Hello world')
    A = AutoLogin()
    A.login()
    # input()
