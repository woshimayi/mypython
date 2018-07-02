# -*- coding: UTF-8 -*-

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(1, 10, 2):
	j = 0
	k = 0
	for k in range( (10-i)/2, i, -1):
		print(' ',end='')
	for j in range(1, i+1):
		print('*',end='')
	print()

for i in range(11, 1, -2):
	j = 0
	k = 0
	for j in range(i-1, 1, -1):
		print('*',end='')
	print()
