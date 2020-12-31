# -*- coding: UTF-8 -*-

from functools import reduce #在 python 3 中 使用 导入 reduce，python2 中不用

tn = 0
sn = []

n = int(input('n=:'))
a = int(input('a=:'))

for conut in range(n):
	tn = tn + a
	a =  a *10
	sn.append(tn)
	print(tn)

sn  = reduce(lambda x,y : x+y, sn)

print(sn)