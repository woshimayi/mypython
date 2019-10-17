# -*-coding:utf-8 -*-

import os
import psutil
import time
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

# print psutil.disk_io_counters()
print psutil.disk_partitions()
print 



