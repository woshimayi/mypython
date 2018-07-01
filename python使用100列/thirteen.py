# -*- coding: UTF-8 -*-

for n in range(100,1000):
	# print(n,end=' ')
	i = n/100
	i = i**3
	j = n/10%10
	j = j**3
	k = n%10
	k = k**3

	print('i=%d j=%d k=%d' % (i, j, k))

	l = i + j + k

	if n == l:
		print('n=%d' % n)