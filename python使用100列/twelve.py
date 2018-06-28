# -*- coding: UTF-8 -*-
# 

from math import sqrt
from sys import stdout

h = 0
lead = 1


for m in range(101,200):
	k = int(sqrt(m+1))     #找到最大的除数
	print('m=%d k=%d h=%d' % (m, k, h))

	for i in range(2, k+1):    #为零跳出
		if m%i == 0:
			lead = 0
			break

	if lead == 1:
		# print('m = %-4d' % m)
		h += 1
		if h % 10 == 0:
			print('')
	lead  = 1
print('h: %d' % h)