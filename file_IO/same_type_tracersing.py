# -*- coding: UTF-8 -*-
# 
import os, sys


# 遍历目录 找出某些类型的文件


Audio = []
Pictures = [".jpg", ".jepg", ".png", ".gif", "bmp"]
folder = []
Document = []
Executable = []

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
	function(dir,Pictures)