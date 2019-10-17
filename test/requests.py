# -*- coding: utf-8 -*-

import urllib2
import urllib
import os

# 获取网页html源码
# re = urllib2.Request("http://www.baidu.com")
# r =  urllib2.urlopen(re)

value = {"username": "2638288078@qq.com", "password": "xxxxx"}
data = urllib.urlencode(value)
url = "https://mail.qq.com/"

request = urllib2.Request(url, data)
response = urllib2.urlopen(request)





with open("./456.txt", 'w') as f:
# 	# 读取网页内容
	print >> f, response.read()




