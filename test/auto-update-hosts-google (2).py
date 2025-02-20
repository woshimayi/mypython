#!/usr/bin/env python
# coding: utf-8
# Author : toddlerya
# Date: Jan 18 2015
import urllib.request
import urllib.error
import urllib.parse
import re
import sys
import os

url = "http://www.360kb.com/kb/2_122.html"
req = urllib.request.Request(url)
html = urllib.request.urlopen(req).read()
head_ver = html.find(r'<strong>google hosts </strong><strong>')
ver_before = len("<strong>google hosts </strong><strong>")
tail_ver = html.find(r' </strong>更新')

head_span = html.find('#base services')
tail_span = html.find('#google source end')
raw_hosts = html[head_span:tail_span]
result, number = re.subn(r'<.*>', '', raw_hosts)
pure_hosts, number = re.subn(r' ', ' ', result)
arch = """127.0.0.1 localhost
# The following lines are desirable for IPv6 capable hosts
::1   ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"""

print("Update your host file start!")
# print "Please input your su password"
f = file(r'/tmp/hosts', 'w+')
new_host = [arch, pure_hosts]
f.writelines(new_host)
f.close()

os.system('mv /tmp/hosts /etc/hosts')

print("Update success!")
