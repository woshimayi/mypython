# coding=utf-8

import module.MyClass
import sys
# import module.config

# class selfTest(autoTest):

# 	def __init__(self, config=None):
# 		super(selfTest, self).__init__(config=config)
# 		self.registerTest()		

	# def login_User(self):
	# 	return autoTest.login_User()
		
	# def _enableTelnet(self):
	# 	return autoTest._enableTelnet()

	# def _enable_tftp(self):
	# 	return autoTest._enable_tftp()

	# def local_kernel_web_update(self):
	# 	return autoTest.local_kernel_web_update()

	# def wanConnection(self):   #宽带账户
	# 	return autoTest.wanConnection(wanName = 'zhengsen', wanPasswd = '')

	# def createWanConnection(self):
	# 	return autoTest.passcreateWanConnection(conn_mode= 'Route', serivice_mode = "INTERNET", ip_mode = 'IPv4', mtu = '1492', vlan_flag = True, vlan_id = '1007')

	# def pingWan(self):
	# 	return autoTest.pingWan(DNS = 'www.baidu.com')

	# def registerTest(self):
	# 	register(func = self.login_User())
	# 	register(func = self._enableTelnet())
	# 	register(func = self._enable_tftp())
	# 	register(func = self.local_updata_url())
	# 	register(func = self.createWanConnection())
	# 	register(func = self.pingWan())

	# def run(self):
	# 	return run()


if __name__ is '__main__':

	G = module.MyClass.autoTest()
	G.loginUser()
	G._enableTelnet()
	G._enable_tftp()

	G.local_kernel_web_update()
	G.wanConnection(wanName = 'zhengsen', wanPasswd = '')
	G.createWanConnection()
	G.pingWan()