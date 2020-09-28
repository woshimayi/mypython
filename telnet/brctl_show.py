# coding=utf-8
#
import logging
import os
import socket
import sys
import shutil

# import win32gui
# import win32api
# import win32con

# import telnetlib
# import SendKeys
import unittest
import time
import re
import datetime

import selenium.webdriver.support.ui as UI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import telnetlib
import threading

# from inLine import execute_shell_telnet
# from inLine import getCurStartupartition


logging.basicConfig(
    level=logging.ERROR,
    format='[%(funcName)s:%(lineno)d] - %(levelname)s:    %(message)s')

user_name = 'root'
pass_wd = 'admin'


login_url = 'http://192.168.1.1/login.html'
mainurl = 'http://192.168.1.1/main.html'
serice_ctrl_url = 'http://192.168.1.1/scsrvcntr.html'
local_updata_url = 'http://192.168.1.1/upload.html'
upgrade_file_path = r'D:\python27\login_html\\123.txt'
factoryurl = 'http://192.168.1.1/factorymode.html'


class autoTest(object):
    def __init__(self, config=None):
        if config is None:
            config = ''

        self.functbl = []
        # self.driver = None
        # self.telnet_count	 = None
        # self.tftp_count  = 0
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        # self.driver.maximize_window()
        # self.driver.set_window_size(100, 40)

    def loginUser(
            self,
            loginurl=login_url,
            mainurl=mainurl,
            username=user_name,
            passwd=pass_wd):
        print('=====login=====')

        print(self.driver.get(loginurl))
        print('=====logining===== %s' % self.driver.current_url)
        time.sleep(0.5)
        if loginurl == self.driver.current_url:
            self.driver.find_element_by_id('LOGIO_TEXT_UserName').clear()  # 清理
            self.driver.find_element_by_id(
                'LOGIO_TEXT_UserName').send_keys(username)
            self.driver.find_element_by_id(
                "LOGIO_PWD_Password").clear()  # 清除对象的内容
            self.driver.find_element_by_id(
                "LOGIO_PWD_Password").send_keys(passwd)  # 在对象上模拟按键键入
            self.driver.find_element_by_id("BTN_Login").click()  # 点击
            time.sleep(2)

        if mainurl != self.driver.current_url:  # 获取当前页面的网址
            self.driver.find_element_by_id('LOGIO_TEXT_UserName').clear()  # 清理
            self.driver.find_element_by_id(
                'LOGIO_TEXT_UserName').send_keys(username)
            self.driver.find_element_by_id(
                "LOGIO_PWD_Password").clear()  # 清除对象的内容
            self.driver.find_element_by_id(
                "LOGIO_PWD_Password").send_keys(passwd)  # 在对象上模拟按键键入
            self.driver.find_element_by_id("BTN_Login").click()  # 点击
            time.sleep(0.5)
        else:
            print('login success')

        # print('login success', self.driver.current_url)
        # if mainurl == self.driver.current_url:
            # self.driver.delete_all_cookies()
            # return True

    def _enableTelnet(self):
        print('=====telnetcom=====')
        try:
            # self.telnet_count = self.telnet_count	 + 1
            # if self.telnet_count > 3:
                        # raise

            # if False is self._login(url=self.main_url,username=self.telnet_name, passewd=self.telnet_passwd):
            #	print 'Error: login error'
            #	raise

            self.driver.get(serice_ctrl_url)
            time.sleep(1)

            if True is self.driver.find_element_by_xpath(
                    "//*[@value = 'TELNET']").is_selected():
                return True

            self.driver.find_element_by_xpath("//*[@value = 'TELNET']").click()
            time.sleep(0.4)
            self.driver.find_element_by_id('saveApplyCtx').click()
            time.sleep(0.3)
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
            print('=====telnet===open=====')
        except Exception:

            return False

    def _disenableTelnet(self):
        print('=====disenable telnetcom=====')
        try:
            # self.telnet_count = self.telnet_count	 + 1
            # if self.telnet_count > 3:
                # raise

            # if False is self._login(url=self.main_url,username=self.telnet_name, passewd=self.telnet_passwd):
            #	print 'Error: login error'
            #	raise

            self.driver.get(serice_ctrl_url)
            time.sleep(1)

            if True is self.driver.find_element_by_xpath(
                    "//*[@value = 'TELNET']").is_selected():
                self.driver.find_element_by_xpath(
                    "//*[@value = 'TELNET']").click()
                time.sleep(0.3)
                self.driver.find_element_by_id('saveApplyCtx').click()
                time.sleep(0.2)
                print('=====telnet===close=====')
                return True

            # self.driver.find_element_by_xpath("//*[@value = 'TELNET']").click()
            # time.sleep(0.3)
            # self.driver.find_element_by_id('saveApplyCtx').click()
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
        except Exception:

            return False

    def _enable_tftp(self):
        print('=====tftp=====')
        try:
            time.sleep(3)
            self.driver.get(serice_ctrl_url)

            if True is self.driver.find_element_by_xpath(
                    "//*[@value = 'TFTP']").is_selected():
                print('tftp is checked')
                return True

            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@value = 'TFTP']").click()
            time.sleep(0.5)
            self.driver.find_element_by_id('saveApplyCtx').click()
            # self.driver.quit()

            # driver = None
            # tftp_count = 0
            return True

        except Exception as e:
            print(e)
            raise

    def register(self, func=None):
        try:
            print('=====register=====')
            self.functbl.append(func)
        except Exception:
            print('register function error:%s' % func)
            print(e)
            raise

    def run(self):
        try:
            print('=====run=====')
            for i in range(0, len(self.functbl)):
                func = self.functbl[i]
                print(
                    'start %d st test:%s function' %
                    ((i + 1), func.__name__))

                if True is func():
                    print('	 success')
                else:
                    print('	 failed')
        except Exception:
            print(e)
            return False

    def local_kernel_web_update(self):
        print('=====update=====')
        try:
            # if False is self._enableTelnet():
            #	print('error: enable telnet error')
            #	return False

            # print("here is :",__file__,sys._getframe().f_lineno)

            # partition_index = getCurStartupartition()
            # print(partition_index)

            # print("here is :",__file__,sys._getframe().f_lineno)

            time.sleep(0.5)
            # if False is self._login(url= self.login_url, mainurl = self.mainurl, username = self.user_name, passwd = self.pass_word):
            #	print 'error : login error'
            #	return False

            self.driver.get(local_updata_url)
            # print("here is :",__file__,sys._getframe().f_lineno)
            time.sleep(0.5)

            self.driver.find_element_by_xpath("//*[@value = '4']").click()
            time.sleep(0.3)
            self.driver.find_element_by_name("FW_UploadFile").click()
            time.sleep(0.3)
            # param1：窗口类名
            # param2：窗口的标题
            # return： 返回窗口的句柄，失败返回0
            dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框

            # param1：要查找子窗口的父窗口句柄 为0则函数一桌面为父窗口，查找桌面的所有子窗口
            # param2：子窗口句柄 子窗口必须是parent 窗口的直接子窗口
            # parent3：类名
            # parent4：窗口名
            # 如果 child 是0 查找从parent 窗口的直接子窗口开始
            # 如果parent 和child 同时 为0 则函数从所有的顶层窗口及消息开始
            ComboBoxEx32 = win32gui.FindWindowEx(
                dialog, 0, 'ComboBoxEx32', None)  # 寻找 文件上传的 子对话框

            ComboBox = win32gui.FindWindowEx(
                ComboBoxEx32, 0, 'ComboBox', None)  # 是edit框和下拉框的组合

            Edit = win32gui.FindWindowEx(
                ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄

            button = win32gui.FindWindowEx(
                dialog, 0, 'Button', None)  # 确定按钮Button

            win32gui.SendMessage(
                Edit,
                win32con.WM_SETTEXT,
                None,
                r'D:\资料\公司资料\hangyan\\tclinux_osgi.bin')  # 往输入框输入绝对地址

            win32gui.SendMessage(
                dialog, win32con.WM_COMMAND, 1, button)  # 按button

            # self.find_element_by_xpath("input[@value = 'Update
            # Software']").click()  #updata software

            self.driver.find_element_by_id('btnOK').click()

            print("upgrade success :", sys._getframe().f_lineno)
            time.sleep(80)
            print(self.driver.close())
            print("web close :", sys._getframe().f_lineno)
            # print("web quit :",__file__,sys._getframe().f_lineno)
            # print("here is :",__file__,sys._getframe().f_lineno)
            # self.driver.quit()
            # partition_index2	=  getCurStartupartition()
            # if False is partition_index2:
            #	return False

            # if partition_index1 is partition_index2:
            #	print 'error: updata failed startup partion is the in upgradng process %s\n' % partition_index2
            #	return False

            # if self.driver is not None:
            #	self.driver.quit()

            # print e, 'local '
        except Exception:
            if self.driver is not None:
                self.driver.close()
                return False

    def wanConnection(self, wanName='zhengsen', wanPasswd=''):
        print('=====wan=====')
        try:
            self.driver.get(mainurl)
            time.sleep(1)

            self.driver.find_element_by_id("MENU_FST_Net").click()  # 网络设置
            time.sleep(0.5)

            self.driver.find_element_by_id('MENU_SEC_NetTr69').click()  # 远程连接
            time.sleep(0.5)

            self.driver.find_element_by_id(
                'MENU_THD_NetLoidAuth').click()  # 宽带识别码
            time.sleep(0.5)

            self.driver.switch_to_frame("mainFrameid")  # 窗口界面跳转
            time.sleep(1)

            self.driver.find_element_by_id('LOID_TEXT_ID').clear()
            time.sleep(0.5)
            self.driver.find_element_by_id('LOID_TEXT_ID').send_keys(wanName)
            time.sleep(0.5)

            self.driver.find_element_by_id('LOID_TEXT_PWD').clear()
            time.sleep(0.5)
            self.driver.find_element_by_id(
                'LOID_TEXT_PWD').send_keys(wanPasswd)
            time.sleep(0.5)

            self.driver.find_element_by_id('BTN_Apply').click()
            time.sleep(2)
            print('=====wan--success=====')
        except Exception:
            if self.driver is not None:
                self.driver.quit()
                return False

    def createWanConnection(
            self,
            closeIE=True,
            conn_mode='Route',
            serivice_mode="INTERNET",
            ip_mode='IPv4',
            mtu='1492',
            vlan_flag=True,
            vlan_id='1007'):
        print('=====Wanconnection=====')
        try:

            self.driver.get(mainurl)
            time.sleep(0.5)

            self.driver.find_element_by_id("MENU_FST_Net").click()  # 点击
            time.sleep(0.5)

            self.driver.find_element_by_id('MENU_THD_NetWan').click()
            time.sleep(0.5)

            self.driver.find_element_by_id('MENU_SEC_NetWan').click()
            time.sleep(0.5)

            self.driver.switch_to_frame("mainFrameid")  # 窗口界面跳转
            time.sleep(1)

            self.driver.find_element_by_id(
                "WAN_SEL_WanLinkName").find_elements_by_tag_name("option")[1].click()

            # 模式选择
            Select(self.driver.find_element_by_id('WAN_SEL_WanConnMode')
                   ).select_by_visible_text(conn_mode)
            time.sleep(1)

            # Select(self.driver.find_element_by_tag_name('select')).select_by_index('6')
            # time.sleep(1)
            # ip模式
            Select(self.driver.find_element_by_id('WAN_SEL_WanIpMode')
                   ).select_by_visible_text(ip_mode)
            time.sleep(1)

            self.driver.find_element_by_id(
                'WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_id(
                'WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_id(
                'WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_id(
                'WAN_TEXT_Mtu').send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_id('WAN_TEXT_Mtu').send_keys(mtu)
            time.sleep(1)

            # if	self.driver.find_element_by_xpath('//input[@id = WAN_CHX_Vlan]').click():
            #	pass

            if True is self.driver.find_element_by_id(
                    "WAN_CHX_Vlan").is_selected():
                print('vlan is checked')
            else:
                self.driver.find_element_by_id("WAN_CHX_Vlan").click()
                time.sleep(0.5)
                self.driver.find_element_by_id(
                    'WAN_TEXT_VlanId').send_keys(vlan_id)
                time.sleep(1)

            self.driver.find_element_by_id('BTN_Apply').click()
            time.sleep(3)

            print('=====Wanconnection-success=====')

        except Exception as e:
            raise

    def pingWan(self, DNS='www.baidu.com'):
        try:
            self.driver.get(mainurl)
            time.sleep(1)

            self.driver.find_element_by_id("MENU_FST_Diag").click()  # 诊断
            time.sleep(0.5)

            self.driver.find_element_by_id(
                'MENU_THD_DiagNetPing').click()  # ping测试
            time.sleep(0.5)

            # self.driver.find_element_by_id('mainFrameid').click()	 #mainframid 点击进入设置页面
            # time.sleep(0.5)

            print('1')
            self.driver.switch_to_frame("mainFrameid")  # 窗口界面跳转
            time.sleep(1)

            self.driver.find_element_by_id('DIAG_TEXT_PingIpaddr').clear()
            time.sleep(0.5)
            self.driver.find_element_by_id(
                'DIAG_TEXT_PingIpaddr').send_keys(DNS)
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

    def getMacAddr(self, num):
        try:
            import xlrd
            import xlutils.copy

            self.driver.get(factoryurl)
            time.sleep(1)
            macAddr = self.driver.find_element_by_xpath(
                '//*[@id="MacAddr"]').get_attribute("value")
            print(macAddr)

            data = xlrd.open_workbook(r'.\20180821.xlsx')
            ws = xlutils.copy.copy(data)
            table = ws.get_sheet(0)
            table.write(num, 8, macAddr)
            ws.save(r'.\20180821.xlsx')

        except Exception as e:
            raise e


def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "list"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    return type


list = []


def do_telnet(Host, username, password, finish, commands):
    '''Telnet远程登录：Windows客户端连接Linux服务器'''

    try:
        # 连接Telnet服务器
        tn = telnetlib.Telnet(Host, port=23, timeout=10)
        # tn.set_debuglevel(1)  # log 打印
        # 输入登录用户名
        tn.read_until('EX6470 login: '.encode())
        tn.write(username.encode() + b'\r\n')
        # 输入登录密码
        tn.read_until('Password: '.encode())
        tn.write(password.encode() + b'\r\n')
        # 登录完毕后执行命令
        tn.read_until(finish.encode())
        global list
        list.clear()
        for command in commands:
            # print('cmd', command)
            tn.write(b'%s\r\n' % command.encode())
            a = []
            b, c, d = tn.expect(a, timeout=1)
            results = str(d, encoding='utf-8').split('\r\n')
            # print('results', results.split('\r\n'))

            for result in results:
                # print(result)
                if 'ra0' in result.strip():
                    # print(result)
                    list.append(result.strip())
                elif 'fc:2a:9c:4b:8d:d1' in result.strip():
                    list.append(result.strip())
            time.sleep(1)

        # 执行完毕后，终止Telnet连接（或输入exit退出）
        tn.read_until(finish.encode())
        tn.close()  # tn.write('exit\n')
        # print('list', list)
        if len(list) >= 2:
            # print(list)
            pass
        return list
    except BaseException as e:
        print(e)
        return

# 判断ip 端口是否存活


def socket_connect(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))

    if 0 == result:
        print("Port is open", end='')
        return True
    else:
        print("Port is not open，return code：%s" % result)
        return False


if __name__ == '__main__':
    Host = '192.168.1.250'  # Telnet服务器IP
    br0 = '192.168.1.250'
    username = 'admin'   # 登录用户名
    password = 'twsz@2020'  # 登录密码
    finish = 'root@EX6470:~# '	   # 命令提示符
    macNum = 0
    while 1:
        num = 1
        list.clear()
        commands = ['brctl show', 'arp -an', 'protest --restore']
        # commands = ['brctl show', 'arp -an']

        while True:
            if socket_connect(br0, 23):
                print(':  ', br0)
                break
            # else:
            # print('not open', Host)
            # Host = '192.168.1.' + str(int(Host.split('.')[3]) + 1)
        # th1 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
        # th1 = threading.Thread(target=do_telnet, args=(Host, username, password, finish, commands))
        th1 = threading.Thread(
            target=do_telnet,
            args=(
                br0,
                username,
                password,
                finish,
                commands))
        th1.start()
        th1.join(5)  # 5秒超时时间
        if len(list) == 0:
            print('not get ra0 and ios device', list)
            break
        print(list)
        macNum = macNum + 1
        print('macNum', macNum)
        time.sleep(100)
