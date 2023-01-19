#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: download.py.py
@time: 2020/9/30 13:44
@desc: 
'''

# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from Ui_download import Ui_download
import os
import sys
import requests


class downloadThread(QThread):   # 处理后台进程
	download_proess_signal = pyqtSignal(int)    # 槽函数链接变量
	
	def __init__(self, download_url, filesize, fileobj, buffer):
		super(downloadThread, self).__init__()
		self.download_url = download_url
		self.filesize = filesize
		self.fileobj = fileobj
		self.buffer = buffer
	
	def run(self):
		try:
			f = requests.get(self.download_url, stream=True)
			offset = 0
			for chunk in f.iter_content(chunk_size=self.buffer):
				if not chunk:
					break
				self.fileobj.seek(offset)
				self.fileobj.write(chunk)
				offset = offset + len(chunk)
				proess = offset / int(self.filesize) * 100
				self.download_proess_signal.emit(int(proess))
			self.fileobj.close()
			self.exit(0)
		except Exception as e:
			print(e)


class download(QDialog, Ui_download):
	"""
	下载类实现
	"""
	
	def __init__(self, download_url, auto_close=True, parent=None):
		"""
		Constructor

		@download_url:下载地址
		@auto_close:下载完成后时候是否需要自动关闭
		"""
		super(download, self).__init__(parent)
		self.setupUi(self)
		self.progressBar.setValue(0)
		self.downloadThread = None
		self.download_url = download_url
		self.filesize = None
		self.fileobj = None
		self.auto_close = auto_close
		self.download()
	
	def download(self):     # 主进程
		self.filesize = requests.get(self.download_url, stream=True).headers['Content-Length']
		# path = os.path.join(".update", os.path.basename(self.download_url))
		self.fileobj = open("update.bin", 'wb')
		self.downloadThread = downloadThread(self.download_url, self.filesize, self.fileobj, buffer=10240)
		self.downloadThread.download_proess_signal.connect(self.change_progressbar_value)
		self.downloadThread.start()
	
	def change_progressbar_value(self, value):  # 槽函数处理进程
		self.progressBar.setValue(value)
		if self.auto_close and value == 100:
			self.close()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ui = download("http://192.168.1.100:8080/lede-mediatek-mt7629-MTK-7629-RFB-squashfs-sysupgrade.bin")
	ui.show()
	sys.exit(app.exec_())