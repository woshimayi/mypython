# -*- coding: UTF-8 -*-


# from sys import stdout
# for j in range(2,1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1,j):
#             if j % i == 0:
#                 n += 1
#                 s -= i
#                 k.append(i)
    
#     if s == 0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print(k[n])
# ================================================

for j in range(2,1001):
	k = []
	sum = 0
	# print(j)
	for i in range(1, j):
		if j%i == 0:
			sum += i
			k.append(i)

	if j == sum:
		print(k)
		print(j)
