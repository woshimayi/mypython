# -*-coding:utf-8 -*-


# import win32gui, win32con
import sys
import sys
from PIL import ImageGrab



# dialog =       win32gui.FindWindow('#32770', u'TeamViewer')  # 对话框

# print dialog

# param1：要查找子窗口的父窗口句柄 为0则函数一桌面为父窗口，查找桌面的所有子窗口
# param2：子窗口句柄 子窗口必须是parent 窗口的直接子窗口
# parent3：类名
# parent4：窗口名
# 如果 child 是0 查找从parent 窗口的直接子窗口开始
# 如果parent 和child 同时 为0 则函数从所有的顶层窗口及消息开始
# ComboBoxEx32 = win32gui.FindWindowEx(dialog, '00080060', 'Edit', None)   #寻找 文件上传的 子对话框

# print ComboBoxEx32

# ComboBox =     win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)  #是edit框和下拉框的组合

# Edit = 	       win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄

# button =       win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

# win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, upgrade_file_path)  # 往输入框输入绝对地址

# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
# time.sleep(1)	

os.system('"C:\\Program Files\\TeamViewer\\TeamViewer.exe"')

path="D:\\"
filename="win.jpg"
im=ImageGrab.grab()
im.save(path+filename)