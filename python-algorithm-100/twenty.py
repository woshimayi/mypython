# -*- coding: UTF-8 -*-

sum = 0
h = 100
time = 10
k = []

for i in range(1, time+1):
	if i == 1:
		sum = h
		k.append(h)
	else:
		sum += h*2
	h /= 2
	k.append(h)

print(k)
print(sum, h)