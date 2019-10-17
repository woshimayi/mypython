# -*- coding: UTF-8 -*-


for i in range(1, 10):
	print(i,end=' ')
	for j in range(1, i+1):
		print("%d*%d=%d" % (i, j, i*j), end=" ")
	print()