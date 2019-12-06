# code=utf-8

import subprocess
import win32api
import os

#执行路径程序
# os.startfile('C:\Program Files\\TeamViewer\\TeamViewer.exe')
# subprocess.call(['C:\\Program Files\\TeamViewer\\TeamViewer.exe'])
# os.system('"C:\\Program Files\\TeamViewer\\TeamViewer.exe"')
# win32api.WinExec('C:\\Program Files\\TeamViewer\\TeamViewer.exe')


image_path = r"X:\HGU\platform\build\43.96856GWOVS\target\UNKNOWN-TW.TW-HGU_S304__R1B01Dac863219-10fd87d0_secureboot_ram_kernel_fs.img"


# os.system('C:\\Windows\\System32\\calc.exe')
# 
# 
print('curl --form "filename=@"' + image_path + " " + "http://192.168.1.1/upload.cgi")

os.system('curl  --form "filename=@"' + image_path + " " + "http://192.168.1.1/upload.cgi")


