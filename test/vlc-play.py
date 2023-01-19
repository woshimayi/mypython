#!/usr/bin/python3
#coding=utf-8


import os
import _thread
import time

isFinished = True

def startvlc(threadName, delay):
	print('启动线程A')	
	#修改vlc安装地址， 访问的rtsp就可以直接用了
	os.system('E:\\新建文件夹\\e\\测试资料2\\测试软件\\vlc-0.8\\vlc-1.0.3\\vlc.exe udp://@239.1.1.1:6001')
	
def stopvlc(threadName, delay):
	print('启动线程B')
	time.sleep(delay)
	os.system('taskkill /im vlc.exe /f')
	global isFinished
	isFinished = True
	print('改变状态功能完毕{0}'.format(isFinished))

def main():
	print('main函数')
	global isFinished
	isFinished = True
	try:
		while True:
			print('当前状态:{0}'.format(isFinished))
			if isFinished:
				print('进入启动')
				_thread.start_new_thread( startvlc, ("Thread-start", 0, ))
				_thread.start_new_thread( stopvlc, ("Thread-stop", 20, ))
				isFinished = False
			else:
				time.sleep(1)
				pass
	except:
	   print ("Error: 无法启动线程")
	
	print('main 函数退出')

if __name__ == '__main__':
	main()
