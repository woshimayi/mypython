# -*-coding:utf-8 -*-

import os
import psutil
import time
import datetime
# os.system('copy  "D:\python27\\win_api\\dist\\timeview.exe" /y "C:\Users\\zhengsen\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

# for i in range(15):
# 

# a =  psutil.pids() 
# print a
# os.system('notepad')
# time.sleep(3)
# os.system('taskkill /F /IM notepad.exe')

# for i in a:
# 	print i
# 	b  =   psutil.Process(i).name()
# 	print b
# 	if b  == 'notepad':
# 		os.system('taskkill /F /IM notepad.exe')



# print psutil.cpu_times()
# print psutil.cpu_times(percpu=True)
# print psutil.cpu_times().user
# print psutil.cpu_count()
# print psutil.cpu_count(logical=False)
# mem = psutil.virtual_memory()
# print str(mem.total/1024.00/1024/1024) + ' ' + 'G'
# 
# print mem.used
# print mem.free/1024.0/1024/1024

# print psutil.swap_memory()

# print psutil.disk_partitions()
# print psutil.disk_usage('/')
# print psutil.disk_io_counters()
# print psutil.disk_io_counters(perdisk=True)
# print psutil.net_io_counters()
# print psutil.net_io_counters(pernic=True)
# print   datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S")

# a = psutil.pids()
# print a
# for i in a:
# 	print i
# 	print psutil.Process(i).name()
# 	print psutil.Process(i).exe()
# 	print psutil.Process(i).cwd()
	# print psutil.Process(i).status()
	# print psutil.Process(i).create_time()
	# print psutil.Process(i).cpu_times()
	# print psutil.Process(i).cpu_affinity()
	# print psutil.Process(i).()

# b =  psutil.Process(4776).exe()
# print 'b' + '=', b

# print os.getenv('PATH')    # 获取环境变量

a = os.path.abspath('.')   # 获取当前目录的绝对路径
print 'a' + '=', a

b = os.path.join('D:\python27\win_api', 'testdir')  #显示一个目录
print b

os.mkdir(b)   #创建一个目录
time.sleep(3)
print os.path.splitext(b)
os.rmdir(b)