# #coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.support.select import Select
import time

# partinfo = ['qwertyuiop,asdfghjkl,zxcvbnm']

# index = partinfo[0].find('e')

# # print index

# index = partinfo[0][12:13]
# if 's' is index or 'a' is index:
# 	print '1'
# print index
# print partinfo
# 
__import__('partinfo')

url = 'http://192.168.1.1/login.html'

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)
driver.get(url)

if url == driver.current_url:   #获取当前页面的网址
				driver.find_element_by_id('LOGIO_TEXT_UserName').clear()  #清理
				driver.find_element_by_id('LOGIO_TEXT_UserName').send_keys(username)
				driver.find_element_by_id("LOGIO_PWD_Password").clear()   #清除对象的内容
				driver.find_element_by_id("LOGIO_PWD_Password").send_keys(passwd)   #在对象上模拟按键键入
				driver.find_element_by_id("BTN_Login").click()   #点击
				time.sleep(1.5)
