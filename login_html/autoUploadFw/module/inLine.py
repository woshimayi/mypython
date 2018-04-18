# coding=utf-8

# import config

Host = '192.168.1.1'

telnet_name = 'telnetadmin'
telnet_passwd = 'telnetadmin'

import sys

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
		return False


def getCurStartupartition():
	try:
		partinfo = None
		
		if 1:
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
		return False


if __name__ is '__main__':
	try:
		getCurStartupartition()
		execute_shell_telnet()
	except Exception,e:
		raise