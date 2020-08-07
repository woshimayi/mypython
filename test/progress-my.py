#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: progress-my.py
@time: 2020/8/6 14:05
@desc: 
'''

import sys
import threading
import time

var = 0

# 进度条
# def progress_bar(num):
# 	for i in range(1, 101):
# 		print("\r", end="")
# 		print('num', num)
# 		if num == 100:
# 			i = 100
# 			print("{}%: ".format(i), "▋" * (i // 2), end="")
# 		else:
# 			print("{}%: ".format(i), "▋" * (i // 2), end="")
# 		sys.stdout.flush()
# 		time.sleep(0.05)

def progress_bar():
	global var
	num = 0
	while 1:
		print("\r", end="")
		if var < 100:
			print("{}%: ".format(num), "▋" * (num // 2), end="")
		else:
			print("{}%: ".format(var), "▋" * (var // 2), end="")
		sys.stdout.flush()
		time.sleep(0.05)
		num = var
		if num > 100:
			return

def progress_bar_time():
	scale = 50
	print("执行开始，祈祷不报错".center(scale // 2,"-"))
	start = time.perf_counter()
	for i in range(scale + 1):
		a = "*" * i
		b = "." * (scale - i)
		c = (i / scale) * 100
		dur = time.perf_counter() - start
		print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
		time.sleep(0.1)
	print("\n"+"执行结束，万幸".center(scale // 2,"-"))


# 简单GUI 进度条
import PySimpleGUI as sg

def progress_bar_GUI():
	mylist = [1,2,3,4,5,6,7,8]
	for i, item in enumerate(mylist):
		sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
		time.sleep(1)


def progress_bar_1():
	for i in range(0, 101, 2):
		time.sleep(0.3)
		num = i // 2
		if i == 100:
			process = "\r[%3s%%]: |%-50s|\n" % (i, '|' * num)
		else:
			process = "\r[%3s%%]: |%-50s|" % (i, '|' * num)
		print(process, end='', flush=True)


# import sys, time
# class ShowProcess():
# 	"""
# 	显示处理进度的类
# 	调用该类相关函数即可实现处理进度的显示
# 	"""
# 	i = 0  # 当前的处理进度
# 	max_steps = 0  # 总共需要处理的次数
# 	max_arrow = 50  # 进度条的长度
#
# 	# 初始化函数，需要知道总共的处理次数
# 	def __init__(self, max_steps):
# 		self.max_steps = max_steps
# 		self.i = 0
#
# 	# 显示函数，根据当前的处理进度i显示进度
# 	# 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
# 	def show_process(self, i=None):
# 		if i is not None:
# 			self.i = i
# 		else:
# 			self.i += 1
#
# 		num_arrow = int(self.i * self.max_arrow / self.max_steps)  # 计算显示多少个'>'
# 		num_line = self.max_arrow - num_arrow  # 计算显示多少个'-'
# 		percent = self.i * 100.0 / self.max_steps  # 计算完成进度，格式为xx.xx%
# 		process_bar = '[' + '>' * num_arrow + '-' * num_line + ']' \
# 					  + '%.2f' % percent + '%' + '\r'  # 带输出的字符串，'\r'表示不换行回到最左边
# 		sys.stdout.write(process_bar)  # 这两句打印字符到终端
# 		sys.stdout.flush()
#
#
# 	def close(self, words='done'):
# 		print
# 		''
# 		print
# 		words
# 		self.i = 0
#
#
# if __name__ == '__main__':
# 	max_steps = 100
#
# 	process_bar = ShowProcess(max_steps)
#
# 	for i in range(max_steps + 1):
# 		process_bar.show_process()
# 		time.sleep(0.05)
# 		process_bar.close()

def do_num():
	global var
	while var < 100:
		var = var + 1
		time.sleep(0.1)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		str = sys.argv[1]
	else:
		str = '112233445566'

	# num = 0;
	# while 1:
	# 	th1 = threading.Thread(target=progress_bar, args=(num))
	# th1.start()
	# th1.join(5)  ##20秒超时时间

	th2 = threading.Thread(target=progress_bar)
	th1 = threading.Thread(target=do_num)

	th1.start()
	th2.start()

	# while 1:
	# 	time.sleep(0.5)
	# 	print(var, end='')

	th1.join(5)
	th2.join(5)

	sys.exit()