# coding=utf-8


import os

def deleteFiles(suffix='.pyc'):   
	curdir=os.getcwd()   #返回当前文件目录
	for root , dirs, files in os.walk(curdir):    
		for name in files:
			if name.endswith(suffix):
				os.remove(os.path.join(root, name))

				print ("Delete File: " + os.path.join(root, name))

	os.system("pause")
	
if __name__ == '__main__':
	deleteFiles()