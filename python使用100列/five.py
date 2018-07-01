# -*- coding: UTF-8 -*-
#

# x = int(input('x:'))
# y = int(input('y:'))
# z = int(input('z:'))

# tmp = 0
# if x > y:
# 	tmp = x
# 	x = y
# 	y = tmp

# print('x', x ,'y',  y)

# tmp = 0
# if x > z:
# 	tmp = x
# 	x = z
# 	z = tmp

# print('x:',x,'\ny:',y,'\nz:',z)

l = []
for i in range(3):
	x = int(input('integer: '))
	l.append(x)
l.sort()
print(l)