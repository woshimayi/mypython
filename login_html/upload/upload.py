#coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Firefox()

#�ű�Ҫ��upload_file.htmlͬһĿ¼
file_path =  'file:///' + os.path.abspath('upload_file.html')
driver.get(file_path)

time.sleep(2)
#��λ�ϴ���ť����ӱ����ļ�
driver.find_element_by_name("file").send_keys('D:\python27\login_html\\123.txt')
time.sleep(2)

driver.quit()