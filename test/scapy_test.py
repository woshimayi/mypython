# -- coding: utf-8 --
from scapy.all import *
 
#数据包应用层数据部分
data='wangpeng'
#发送端IP地址10.0.3.83不是本机ip地址   目的端IP地址不详      传输层的TCP并未指明数据包类型：syn fin ack 窗口大小 数据包如果分片，要指明序号
pkt=IP(src='192.168.1.100',dst='192.168.1.2')/TCP(sport=12345,dport=5555)/data
#间隔一秒发送一次   总共发送5次   发送网卡口：enp1s0

send(pkt,inter=1,count=5,iface="enp1s0") 