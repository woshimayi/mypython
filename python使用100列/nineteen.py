# -*- coding: UTF-8 -*-

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