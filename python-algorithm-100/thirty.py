# -*- coding: UTF-8 -*-
# 

s = '1234321'

for j in range(100, 1000000):
	l = len(str(s))
	for i in range(int(l/2)):
		if s[i] != s[l-1]:
			break
		print(s)

print()