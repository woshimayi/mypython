# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:29:44 2016

@author: zhang
"""

import os
import sys
import time
#from fabric.api import *
#from fabric.context_managers import *
#from fabric.contrib.files import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from glob import glob
import SendKeys
from selenium.webdriver.support.select import Select

def buildS304(projectPath, buildOptions):
	env.host_string = '10.58.100.198'
	env.user = 'sunbao'
	env.password = 'sunbao'
	with cd(projectPath + '/platform'):
		run('make rootfs ' + buildOptions)
		run('make install')
		run('make image.w')


def releaseImage(projectPath, buildOptions, imagePath, releasePath):
	env.host_string = '10.58.100.198'
	env.user = 'sunbao'
	env.password = 'sunbao'
	with cd(projectPath + '/platform'):
		run('git clean -dfx -- . ../products')
		run('git reset --hard')
		run('git pull -r')
		run('make rootfs ' + buildOptions)
		run('make install')
		run('make image.w')
	releasePath = releasePath + time.strftime('%Y%m%d')
	if not os.path.exists(releasePath):
		os.mkdir(releasePath)
	get(imagePath + '*.w', releasePath)
	get(imagePath + '*.img', releasePath)


def loginWeb(baseUrl):
	logUrl = baseUrl + '/login.html'
	mainUrl = baseUrl + '/main.html'
	try:
		driver = webdriver.Firefox()
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get(logUrl)
		time.sleep(1)
		if mainUrl == driver.current_url:
			print 'Already login'
			return driver
		if logUrl == driver.current_url:    
			driver.find_element_by_id("LOGIO_PWD_Password").send_keys("nE7jA%5m")
			driver.find_element_by_id("BTN_Login").click()
		time.sleep(1)
		if mainUrl == driver.current_url:
			print 'Login succ'
			return driver
		else:
			print 'Login fail'
			return None
	except Exception as why:
		print why
		return None


def upgradeImage(baseUrl, imageName):
	try:
		driver = loginWeb(baseUrl)
		if None == driver:
			return
		time.sleep(2)
		driver.get(baseUrl + '/upload.html')
		driver.find_element_by_name("filename").click()
		SendKeys.SendKeys(imageName)
		SendKeys.SendKeys("{ENTER}")
		driver.find_element_by_xpath("/html/body/blockquote/form/p/input").click()
	except Exception as why:
		print why


def enableTelnet(baseUrl, enable):
	try:
		driver = loginWeb(baseUrl)
		if None == driver:
			return
		time.sleep(2)
		driver.get(baseUrl + '/scsrvcntr.html')
		if driver.find_element_by_xpath('//*[@id="serviceList"]/tr[2]/td[2]/input').is_selected():
			if enable:
				driver.quit()
				return
		else:
			if not enable:
				driver.quit()
				return
		driver.find_element_by_xpath('//*[@id="serviceList"]/tr[2]/td[2]/input').click()
		driver.find_element_by_id('saveApplyCtx').click()
		time.sleep(2)
		driver.quit()
	except Exception,why:
		print why


def loginCsp():
	try:
		driver = webdriver.Firefox()
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get('https://support.broadcom.com/')
		driver.find_element_by_id("TxtUserName").send_keys("yanchunping@twsz.com")
		driver.find_element_by_id("TxtPassword").send_keys("Twshponbu2012")
		time.sleep(1)
		driver.find_element_by_id("BtnLogin").click()
		return driver
	except Exception as why:
		print why
		return None


def createCsp():
	try:
		driver = loginCsp()
		time.sleep(2)
		driver.find_element_by_link_text("Product Cases").click()
	except Exception as why:
		print why
		return None


def updateCsp(cspId):
	try:
		driver = loginCsp()
		time.sleep(2)
		driver.find_element_by_link_text("Product Cases").click()
		time.sleep(3)
		driver.find_element_by_link_text("Search Cases").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ctl00_TxtCaseID").send_keys(cspId)
		driver.find_element_by_id("ctl00_ctl00_BtnSearch2").click()
		time.sleep(5)
		driver.find_element_by_link_text(cspId).click()
	except Exception as why:
		print why
		return None


def enableMirror(baseUrl, enable):
	try:
		driver = loginWeb(baseUrl)
		if None == driver:
			return
		driver.get(baseUrl + '/engdebug.html')
	except Exception,why:
		print why

		
def testDhcpv6(baseUrl):
	try:
		driver = loginWeb(baseUrl)
		if None == driver:
			return
		flag = 1
		idx  = 1
		while True:
			driver.get(baseUrl + '/wan_setup.html')
			time.sleep(2)

			if 1 == flag:
				driver.find_element_by_id("WAN_TEXT_VlanId").clear()
				driver.find_element_by_id("WAN_TEXT_VlanId").send_keys("3338")
				if driver.find_element_by_id("WAN_CHX_Enblunnumbered").is_selected():
					driver.find_element_by_id("WAN_CHX_Enblunnumbered").click()
					print '3338_1'
				flag = -1;
			elif -1 == flag:
				driver.find_element_by_id("WAN_TEXT_VlanId").clear()
				driver.find_element_by_id("WAN_TEXT_VlanId").send_keys("3333")
				if driver.find_element_by_id("WAN_CHX_Enblunnumbered").is_selected():
					pass
					print '3333_1'
				else:
					driver.find_element_by_id("WAN_CHX_Enblunnumbered").click()
					print '3333_2'
				flag = 1;

			driver.find_element_by_id("BTN_Apply").click()
			print "Try " ,idx ,"time"
			time.sleep(60)
			driver.get(baseUrl + '/wan_status_v6.html')
			time.sleep(2)
			save_fn = "C:\\Users\\sunbao\\Desktop\\selTest\\%d.png" % idx
			driver.get_screenshot_as_file(save_fn)
			print 'ok'
			idx += 1
			time.sleep(2)
	except Exception,why:
		print why

if __name__ == '__main__':
	projectPath = '~/S304/'
	buildOptions = 'PRODUCT=31+dbus SF=ct BOARD=vb7'
	imagePath = '~/S304/platform/build/31.96838GWOVS/'
	releasePath = 'C:\\Work\\Project\\ESurfing2.0\\Release\\'
	imageName = 'V:\\S304\\platform\\build\\31.96838GWOVS\\31.*_ct_dbus_git*.img'
	wimageName = 'V:\\S304\\platform\\build\\31.96838GWOVS\\31.*.w'
	baseUrl = 'http://192.168.1.1:8080'

	if 1 == len(sys.argv):
		menu = """
****************
   IWE - S304   
----------------
0. quit
1. Release
2. Build
3. Upgrade
4. Enable telnet
5. Disable telnet
6. Create CSP
7. Update CSP
8. Enable mirror
9. Disable mirror
a. test dhcpv6
****************
Please select:"""
		try:
			taskList = raw_input(menu).strip()[0].lower()
		except (EOFError, KeyboardInterrupt,IndexError):
			taskList = '0'
	else:
		taskList = sys.argv[1]

	for task in taskList:
		if task is '0':
			break
		elif task is '1':
			print '>Task#1: Release...'
			releaseImage(projectPath, buildOptions, imagePath, releasePath)
		elif task is '2':
			print '>Task#2: Build...'
			buildS304(projectPath, buildOptions)
		elif task is '3':
			print '>Task#3: Upgrade...'
			imageName = glob(imageName)
			upgradeImage(baseUrl, imageName[0])
		elif task is '4':
			print '>Task#4: Enable telnet...'
			enableTelnet(baseUrl, True)
		elif task is '5':
			print '>Task#5: Disable telnet...'
			enableTelnet(baseUrl, False)
		elif task is '6':
			print '>Task#6: Create CSP...'
			createCsp()
		elif task is '7':
			print '>Task#7: Update CSP...'
			cspId = raw_input('Please CSP ID: ')
			if cspId:
				updateCsp(cspId)
		elif task is '8':
			print '>Task#8: Enable mirror...'
			enableMirror(baseUrl, True)
		elif task is '9':
			print '>Task#9: Disable mirror...'
			enableMirror(baseUrl, False)
		elif task is 'a':
			print '>Task#a: test dhcpv6...'
			testDhcpv6(baseUrl)
		else:
			print 'Error Task#' + task
	