# #coding=utf-8

user_name = 'telnetcom'
pass_word = 'nE7jA%5m'

telnet_name = 'telnetadmin'
telnet_passwd = 'telnetadmin'



Host = '192.168.1.1'

login_url = 'http://192.168.1.1/login.html'
mainurl='http://192.168.1.1/main.html'
serice_ctrl_url = 'http://192.168.1.1/scsrvcntr.html'
local_updata_url = 'http://192.168.1.1/upload.html'

upgrade_file_path = 'zhengsen/12334456677889/'


import os
import sys
import shutil

import win32gui
import win32api
import win32con

import telnetlib 
import SendKeys
import unittest, time, re, datetime
			
import selenium.webdriver.support.ui as UI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait





def execute_shell_telnet(shellcmd=None,data=None):
	try:
		print 'data is %s' % data 
		tn = telnetlib.Telnet(Host)
		
		tn.read_until('Login')
		tn.write(telnet_name+ '\n')

		tn.read_until('Password')
		tn.write(telnet_passwd+ '\n\n')

		tn.read_until('S304')
		tn.write('l\n')

		tn.read_until('#')
		tn.write(shellcmd)

		#读取所有匹配到的数据
  		# ra=tn.read_all()
  		# print(type(ra));
  		# print(ra.decode('gbk'));
  		

		content = tn.read_until('#')

		tn.close()

		data.append(content)
		print 'data is %s ' % data
		print __file__,sys._getframe().f_lineno
		return True
	except Exception,e:
		print e
		print 'data is %s ' % data
		print __file__,sys._getframe().f_lineno
		return False


def getCurStartupartition():
	try:
		partinfo = None
		
		if 1:
			print __file__,sys._getframe().f_lineno   #####################
			if True is execute_shell_telnet(shellcmd = 's BootImage\n', data=partinfo):
				index = partinfo[0].find("BootImage:")
				print index
				print __file__,sys._getframe().f_lineno
				if -1  == index:
					print 'error: fail :get startup part info '
					raise
				else:
					partition_no =  partinfo[0][index + 12: index + 13]  # 2
					print "here is :",__file__,sys._getframe().f_lineno	
					if '1' is partition_no or '2' is partition_no:
						print partinfo_no
						return partition_no
					else:
						print 'get startup partition index is error %s' % partition_no
						return False

			elif 1:
				print __file__,sys._getframe().f_lineno	#####################
				index = partinfo[0].find(" :")
				if -1  == index:
					print 'error: fail :get startup part info'
					raise
				else:
					partition_no =  partinfo[0][index + 3: index + 4]
					if '1' is partition_no or '0' is partition_no:
						print partinfo_no
						return partition_no
					else:
						print 'get startup partition index is error %s' % partition_no
						return False
	except Exception, e:
		print e
		print __file__,sys._getframe().f_lineno	
		return False


class autoTest(object):
	def __init__(self, config = None):
	 	if config is None:
			config = ''
			print '================warn============'
			print 'warn: config use default config fron templateConfig.py '
			print '================================'

		self.functbl = []
		self.driver = None
		self.telnet_count  = None
		self.tftp_count  = 0


	def loginUser(self, url=None, mainurl=None, username=None, passwd=None):
		print '=====username====='
		driver = webdriver.Firefox()
		driver.implicitly_wait(10)
		driver.maximize_window()
		time.sleep(1)
		driver.get(url)
		time.sleep(2)

		if url == driver.current_url:   #获取当前页面的网址
			driver.find_element_by_id('LOGIO_TEXT_UserName').clear()  #清理
			driver.find_element_by_id('LOGIO_TEXT_UserName').send_keys(username)
			driver.find_element_by_id("LOGIO_PWD_Password").clear()   #清除对象的内容
			driver.find_element_by_id("LOGIO_PWD_Password").send_keys(passwd)   #在对象上模拟按键键入
			driver.find_element_by_id("BTN_Login").click()   #点击
			time.sleep(3)

		if mainurl == driver.current_url:
			self.driver = driver
			self.driver.delete_all_cookies()
			return True

	# except Exception,e:
	# 	print e
	# 	self.driver = None
	# 	retrun False


	def _enableTelnet(self):
		print '=====telnetcom====='
		try:
			# self.telnet_count = self.telnet_count  + 1
			# if self.telnet_count > 3:
				# raise

			# if False is self._login(url=self.main_url,username=self.telnet_name, passewd=self.telnet_passwd):
			# 	print 'Error: login error'
			# 	raise
			time.sleep(3)

			self.driver.get(serice_ctrl_url)

			if True is self.driver.find_element_by_xpath("//*[@value = 'TELNET']").is_selected():
				print 'telnet is checked'
				return True
			
			self.driver.find_element_by_xpath("//*[@value = 'TELNET']").click()
			time.sleep(1)
			self.driver.find_element_by_id('saveApplyCtx').click()
			time.sleep(3)
			# self.driver.quit()
			# self.driver =None

			if True is enable_telnet():
				# self.telnet_count =  0
				return True
			else:
				raise
			if True is enable_count():
				self.telnet_count = 0
				return True
			else:
				raise
			print '=====telnet===over====='
		except Exception,e:

			return False


	def _enable_tftp(self):
		print '=====tftp====='
		try:
			time.sleep(3)
			self.driver.get(serice_ctrl_url)
			
			if True is self.driver.find_element_by_xpath("//*[@value = 'TFTP']").is_selected():
				print 'tftp is checked'
				return True

			time.sleep(1)
			self.driver.find_element_by_xpath("//*[@value = 'TFTP']").click()
			
			self.driver.find_element_by_id('saveApplyCtx').click()
			# self.driver.quit()
			
			# driver = None
			# tftp_count = 0
			return True
			
		except Exception as e:
			print e
			raise
		


	#生成函数指针链接
	def register(self, func=None):
		try:
			self.functbl.append(func)
		except Exception,e:
			print 'register function error:%s'%func
			print e
			raise 


	#依次执行函数
	def run(self):
		try:
			for i in range(0, len(self.functbl)):
				func=self.functbl[i]
				print 'start %d st test:%s function'%((i + 1), func.__name__)
				if True is func():
					print 'success'
				else:
					print 'failed'
		except Exception,e:
			print e
			return False

	
    

	def local_kernel_web_update(self):
		print '=====update====='
		try:
			if False is self._enableTelnet():
				print 'error: enable telnet error'
				return False

			print "here is :",__file__,sys._getframe().f_lineno


			partition_index = getCurStartupartition()
			print partition_index

			print "here is :",__file__,sys._getframe().f_lineno

			time.sleep(1)
			# if False is self._login(url= self.login_url, mainurl = self.mainurl, username = self.user_name, passwd = self.pass_word):
			# 	print 'error : login error'
			# 	return False

			self.driver.get(local_updata_url)
			time.sleep(1)
			
			self.driver.find_element_by_name("filename").click()
			time.sleep(1)
			
			# param1：窗口类名
			# param2：窗口的标题
			# return： 返回窗口的句柄，失败返回0
			dialog =       win32gui.FindWindow('#32770', u'文件上传')  # 对话框

			# param1：要查找子窗口的父窗口句柄 为0则函数一桌面为父窗口，查找桌面的所有子窗口
			# param2：子窗口句柄 子窗口必须是parent 窗口的直接子窗口
			# parent3：类名
			# parent4：窗口名
			# 如果 child 是0 查找从parent 窗口的直接子窗口开始
			# 如果parent 和child 同时 为0 则函数从所有的顶层窗口及消息开始
			ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)   #寻找 文件上传的 子对话框
 
			ComboBox =     win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)  #是edit框和下拉框的组合

			Edit = 	       win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
			
			button =       win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

			win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\python27\login_html\\123.txt')  # 往输入框输入绝对地址
			
			win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

			# self.find_element_by_xpath("input[@value = 'Update Software']").click()  #updata software

			

			time.sleep(5)
			# self.driver.quit()
			# self.driver = None
			time.sleep(10)

			# if False is self._enableTelnet():
			# 	print 'error: enable telnet error'
			# 	return False

			# partition_index2  =  getCurStartupartition()
			# if False is partition_index2:
			# 	return False

			# if partition_index1 is partition_index2:
			# 	print 'error: updata failed startup partion is the in upgradng process %s\n' % partition_index2
			# 	return False
			
			# if self.driver is not None:
			# 	self.driver.quit()
			
			# print e, 'local '
			# return False
			print '=====upgradng_success====='
		except Exception,e:
			if self.driver is not None:
				# self.driver.quit()
				return False


	def wanConnection(self, wanName = 'zhengsen', wanPasswd = ''):
		print '=====wan====='
		try:
			self.driver.get(mainurl)
			time.sleep(1)

			self.driver.find_element_by_id("MENU_FST_Net").click()   #网络设置
			time.sleep(0.5)

			self.driver.find_element_by_id('MENU_SEC_NetTr69').click()   #远程连接
			time.sleep(0.5)

			self.driver.find_element_by_id('MENU_THD_NetLoidAuth').click()  #宽带识别码
			time.sleep(0.5)

			self.driver.switch_to_frame("mainFrameid")   #窗口界面跳转
			time.sleep(1)

			self.driver.find_element_by_id('LOID_TEXT_ID').clear()
			time.sleep(0.5)
			self.driver.find_element_by_id('LOID_TEXT_ID').send_keys(wanName)
			time.sleep(0.5)

			self.driver.find_element_by_id('LOID_TEXT_PWD').clear()
			time.sleep(0.5)
			self.driver.find_element_by_id('LOID_TEXT_PWD').send_keys(wanPasswd)
			time.sleep(0.5)


			self.driver.find_element_by_id('BTN_Apply').click()
			time.sleep(2)
		except Exception,e:
			if self.driver is not None:
				# self.driver.quit()
				return False





	def createWanConnection(self,closeIE = True, conn_mode= 'Route', serivice_mode = "INTERNET", ip_mode = 'IPv4', mtu = '1492', vlan_flag = True, vlan_id = '1007'):
		print '=====Wanconnection====='
		try:
			
			self.driver.get(mainurl)
			time.sleep(0.5)

			self.driver.find_element_by_id("MENU_FST_Net").click()   #点击
			time.sleep(0.5)

			self.driver.find_element_by_id('MENU_THD_NetWan').click()
			time.sleep(0.5)

			print '===WAN_SEL_WanLinkName==='
			self.driver.switch_to_frame("mainFrameid") #窗口界面跳转
			time.sleep(1)

			
			#1：success
			# Select(self.driver.find_element_by_id('WAN_SEL_WanLinkName')).select_by_value('8')   
			

			#2：success
			# sel = self.driver.find_element_by_id('WAN_SEL_WanLinkName')
			# print sel
			# Select(sel).select_by_value('8')

			#3：success
			# self.driver.find_element_by_xpath("//*[@id='WAN_SEL_WanLinkName']/option[@value='8']").click()
			
			#4： failed
			# self.driver.find_element_by_id('WAN_SEL_WanLinkName').click()
			# time.sleep(1)
			# self.find_element_by_xpath("//*[@id = 'WAN_SEL_WanLinkName' and @value = '8']").click()

			#5： fail
			# self.driver.find_element_by_id("WAN_SEL_WanLinkName").select_by_index('8')
			# time.sleep(1)
			
			#6：success
			# s = self.driver.find_element_by_xpath('//*[@id ="WAN_SEL_WanLinkName"]')
			
			#7：success
			# s.find_element_by_xpath("//option[@value = '8']").click()
			
			#8：success
			# Select(s).select_by_index(1)
			
			#9：success
			# Select(s).select_by_visible_text("新增WAN连接")
			

			self.driver.find_element_by_id("WAN_SEL_WanLinkName").find_elements_by_tag_name("option")[1].click()



			#模式选择
			Select(self.driver.find_element_by_id('WAN_SEL_WanConnMode')).select_by_visible_text(conn_mode)
			time.sleep(1)
			
			
			# Select(self.driver.find_element_by_tag_name('select')).select_by_index('6')
			# time.sleep(1)
			# ip模式
			Select(self.driver.find_element_by_id('WAN_SEL_WanIpMode')).select_by_visible_text(ip_mode)
			time.sleep(1)

			self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
			self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
			self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
			self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)  
			self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(mtu)
			time.sleep(1)


			# if 	self.driver.find_element_by_xpath('//input[@id = WAN_CHX_Vlan]').click():
			# 	pass
			
			if True is self.driver.find_element_by_id("WAN_CHX_Vlan").is_selected():
				print 'vlan is checked'
			else:
				self.driver.find_element_by_id("WAN_CHX_Vlan").click()
				time.sleep(0.5)
				self.driver.find_element_by_id('WAN_TEXT_VlanId').send_keys(vlan_id)  
				time.sleep(1)

			self.driver.find_element_by_id('BTN_Apply').click()
			time.sleep(3)

			print '=====Wanconnection-success====='
		except Exception as e:
			raise

	def pingWan(self, DNS = 'www.baidu.com'):
		try:
			self.driver.get(mainurl)
			time.sleep(1)

			self.driver.find_element_by_id("MENU_FST_Diag").click()   #诊断
			time.sleep(0.5)

			self.driver.find_element_by_id('MENU_THD_DiagNetPing').click()   #ping测试
			time.sleep(0.5)

			# self.driver.find_element_by_id('mainFrameid').click()  #mainframid 点击进入设置页面
			# time.sleep(0.5)

			print '1'
			self.driver.switch_to_frame("mainFrameid")   #窗口界面跳转
			time.sleep(1)

			self.driver.find_element_by_id('DIAG_TEXT_PingIpaddr').clear()
			time.sleep(0.5)
			self.driver.find_element_by_id('DIAG_TEXT_PingIpaddr').send_keys(DNS)
			time.sleep(0.5)

			self.driver.find_element_by_id('BTN_Apply').send_keys(Keys.ENTER)
			time.sleep(2)

			# DIAG_DIV_PingResult# 结果
			sel = self.driver.find_element_by_id('DIAG_DIV_PingResult')
			print(sel)
			# re = ping.find_element_by_xpath('Can not resolve address!')
			# print re

		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
		


if __name__ == '__main__':
	if 1:
		if len(sys.argv) == 2:
			b = autoTest(sys.argv[1])
		else:
			b = autoTest()

		b.register(func = b.loginUser(login_url, mainurl, user_name, pass_word))
		b.register(func = b._enableTelnet())
		b.register(func = b._enable_tftp())
		b.register(func = b.local_kernel_web_update())
		b.register(func = b.wanConnection())
		b.register(func = b.createWanConnection())
		b.register(func = b.pingWan())
			
		b.run()
	else:
		print 'reserve'