#--coding:utf-8--

import urllib
import os

# try:
# 	f  = open('./123.py', 'r')
# 	print f.read()
# finally:
# 	if f:
# 		f.close()


# with open('./123.py', 'r') as f:
# 	print f.read()


# for line in f.readlines():
# 	print(line.strip())


def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	print '1231231231231'
	return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

s= os.path.abspath('.')
s = os.path.join(s, '456.txt')




with open('./456.txt', 'w') as f:
	f.write('#hello world')

	s = '123',
	asd = '467',
	# 信息重定向到文件中
	# print >>f , s, '  \n', asd    
	print >> f, '123', '456'
	# 操作兄台概念名称
	print >> f, os.name
	# 详细的系统信息
	# print >> f, os.uname()
	# 环境变量
	print >> f, os.environ
	# 获取某个系统变量的值
	# print >> f, os.getenv('PATH')
	# 查看当前目录的局对路径
	print >> f, os.path.abspath('.')
	# 在某个目录下创建一个目录
	# 首先把新目录的完整路径标识出来
	# s = os.path.join('D:\\python27', 'testdir')
	# 创建一个目录
	# os.mkdir(s)
	# 删掉一个目录
	# os.rmdir(s)
	# 
	print >> f,  html
#conding = utf-8

# with open(s, 'w') as f:
# 	f.write('#hello world')

