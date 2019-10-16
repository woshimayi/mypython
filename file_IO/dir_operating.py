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


dir = 'D:'

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

# 遍历目录
def function(dir, file):
	print("==========os.walk================")
	index = 1  

	for root,dirs,files in os.walk(dir):
		print("第",index,"层")
		index += 1
		for filepath in files:
			print(os.path.splitext(filepath)[1])
			if os.path.splitext(filepath)[0] == file:
				if file and os.path.splitext(filepath)[1] == '.exe':
					exec = os.path.join(root,filepath)
					os.startfile(exec)
		for sub in dirs:
			pass
			print('dir', os.path.join(root,sub))


if __name__=="__main__":
	# file = input("Enter your input: ")
	# print(file)
	function(dir,r".jpg")