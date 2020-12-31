# -*- coding: UTF-8 -*-

s = 'qwerty'
l = len(s)

# =============================
# def output(s, l):
# 	if l == 0:
# 		return 
# 	print(s[l-1])
# 	output(s, l-1)

# output(s, l)
# =============================

for i in range(l,1, -1):
	# print(i)
	print(s[i-1])