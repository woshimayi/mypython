# -*- coding: UTF-8 -*-

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# ======================================================
# n = 10
# for i in range(1, n, 2):
# 	j = 0
# 	k = 0
# 	for k in range(int((n-i)/2), 0, -1):
# 		print(' ',end='')
# 	for j in range(1, i+1):
# 		print('*',end='')
# 	print()

# for i in range(n-2, 1, -2):
# 	j = 0
# 	k = 0
# 	# print(i)
# 	for j in range(int((n-i)/2), 0, -1):
# 		print(' ',end='')
# 	for k in range(1, i):
# 		print('*',end='')
# 	print()
# ======================================================

n = 10
for i in range(n):
	for k in range(n-i, 1, -1):
		print(' ',end='')
	for j in range(2*i-1):
		print('*',end='')
	print()

for i in range(n):
	# print(i)
	for k in range(i+1):
		print(' ',end='')
	for j in range((n-i-2)*2, 1, -1):
		print('*',end='')
	print()
# ======================================================


