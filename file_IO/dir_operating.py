# -*- coding: utf-8 -*-

import os
import sys
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))

# curron_dir = os.path.abspath('.')
# mkdir = os.path.join(curron_dir, 'test_dir')

# print(os.path.split(mkdir))
# print(os.path.splitext(mkdir))

# if id('test_dir') == id(os.path.split(mkdir)):
# 	print("cunzai")
# else:
# 	os.mkdir(mkdir)
# 	print("sd")
# os.rmdir(mkdir)

# os.rename('test_123', 'test_dir')


# for x in os.listdir('.'):
# 	if os.path.isdir(x):
# 		print(x)

# print('C:\\Windows\\System32')


dir = r'C:\Users\zs\Pictures'

# 打开搜索到的所有程序
# for x in os.listdir(dir):
# 	print(x)
	# if os.path.isdir(dir):
		# print(x)
	# if os.path.splitext(x)[1]=='.exe':
	# 	y = os.path.join(dir, x)
	# 	print(y)


# 循环打开程序
# for z in range(10):
# 	print(z)
# 	os.startfile('calc')b


i = 0;
k = 0;

# def gci(dir):
# 	global i
# 	global k
# 	for x in os.listdir(dir):
# 		if os.path.isdir(x):
# 			# print(x)
# 			k = k + 1
# 			print(k, end='')

# 			y = os.path.join(dir, x)
# 			print(':', y)
# 			print(os.listdir(y))
# 		elif os.path.isfile(x) and os.path.splitext(x)[1] == '.py':
# 			y = os.path.join(dir, x)
# 			# i = i + 1
# 			# print(i, end='')
# 			# print( '::'+ y)


# print(dir)

# gci(dir)

# print(i)

# 遍历目录 找出具体某些类型的文件
# 
dir = r'C:\Users\zs\Pictures'

def function(dir, file):
	print("==========os.walk================")
	index = 1  
	print(file)
	for root,dirs,files in os.walk(dir):
		# print("第",index,"层")
		index += 1
		for filepath in files:
			# print(os.path.splitext(filepath)[0], os.path.splitext(filepath)[1])
			if os.path.splitext(filepath)[1] in file:
				print('file', os.path.join(root,filepath))
					# os.startfile(exec)  # 执行文件
		for sub in dirs:
			print('dir', os.path.join(root,sub))


if __name__=="__main__":
	# file = input("Enter your input: ")
	# print(file)
	function(dir,[".jpg", ".jepg", ".png", ".gif"])