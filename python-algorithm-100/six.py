# -*- coding: UTF-8 -*-

import sys   
sys.setrecursionlimit(10000)

# ======1=====
# def fib(n):
# 	a, b = 1, 1
# 	print(a, end=' ')
# 	for i in range(n+1):
# 		a,b = b,a+b
# 		print(b, end=" ")

# fib(15)
# # for i in range(20):
# print()


# =====2=====
def fib(n):
	if n==1 or n==2:
		return 1
	# print(n)
	return fib(n-1)+fib(n-2)

i = 0
for i in range(20):
	print(fib(i))


# =====3=====