# -*-coding:utf-8 -*-


# import win32gui, win32con
import sys
import sys
from PIL import ImageGrab



# dialog =       win32gui.FindWindow('#32770', u'TeamViewer')  # �Ի���

# print dialog

# param1��Ҫ�����Ӵ��ڵĸ����ھ�� Ϊ0����һ����Ϊ�����ڣ���������������Ӵ���
# param2���Ӵ��ھ�� �Ӵ��ڱ�����parent ���ڵ�ֱ���Ӵ���
# parent3������
# parent4��������
# ��� child ��0 ���Ҵ�parent ���ڵ�ֱ���Ӵ��ڿ�ʼ
# ���parent ��child ͬʱ Ϊ0 ���������еĶ��㴰�ڼ���Ϣ��ʼ
# ComboBoxEx32 = win32gui.FindWindowEx(dialog, '00080060', 'Edit', None)   #Ѱ�� �ļ��ϴ��� �ӶԻ���

# print ComboBoxEx32

# ComboBox =     win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)  #��edit�������������

# Edit = 	       win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # ������������Ѱ�Ҷ���ֱ���ҵ������Edit����ľ��

# button =       win32gui.FindWindowEx(dialog, 0, 'Button', None)  # ȷ����ťButton

# win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, upgrade_file_path)  # �������������Ե�ַ

# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # ��button
# time.sleep(1)	

os.system('"C:\\Program Files\\TeamViewer\\TeamViewer.exe"')

path="D:\\"
filename="win.jpg"
im=ImageGrab.grab()
im.save(path+filename)