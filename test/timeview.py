# coding=utf-8


import os
# import sys
# import subprocess
# import win32api
import time
from PIL import ImageGrab

#执行路径程序
# os.startfile('C:\Program Files\\TeamViewer\\TeamViewer.exe')
# subprocess.call(['C:\\Program Files\\TeamViewer\\TeamViewer.exe'])
os.system('"C:\\Program Files\\TeamViewer\\TeamViewer.exe"')
# win32api.WinExec('C:\\Program Files\\TeamViewer\\TeamViewer.exe')

time.sleep(5)
print 'screen'

path="D:\\"
filename="timeview.jpg"
im=ImageGrab.grab()
im.save(path+filename)

