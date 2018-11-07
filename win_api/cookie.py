# -*- coding: utf-8 -*-

import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
#声明一个cookiejar 对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用URLlib库的HTTPCookProcessor(cookie)
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handker 方法开构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True, ignore_expires=True)

for item in cookie:
	print('Name = ' +item.name)
	print('Value = ' +item.value)