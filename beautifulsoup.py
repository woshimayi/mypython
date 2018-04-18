# coding:utf-8

import sys
import os
from collections import Iterable


# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)


# v  = fact(10)
# print v


# L = []
# n =1
# for n in range(20):
# 	L.append(n)
# 	print L
# print L

# r = []
# for i in range(n):
# 	r.append(L[i])
# 	print r

# print L[5:19]
# print L[:3]
# print L[5:]
# print L[-3:]
# print L[:-3]
# print L[::3]
# print L[:]





# L = list(range(23))
# print L

# d = {'a':1, 'b':2, 'c':3, 'd':4}
# for key in d:
# 	print key 

# for key in d.values():
# 	print key 

# for key, value in d.items():
# 	print key, value


# print isinstance("abc", Iterable)
# print isinstance([1,2,3], Iterable)
# print isinstance(123, Iterable)

# print value

# for i, j in enumerate(['A', 'B', 'C']):
# 	print i, j

# 列表生成器

L = []
# L = list(range(1, 20))
# print L

# for x in range(1, 20):
# 	L.append(x*x)
# 	print L

# L = [x*x for x in range(1, 20)]
# print L

# L = [x*x for x in range(1, 20) if x%3 == 0]
# print L

# L = [m + n for m in 'ABC' for n in 'XYZ']
# print L


L = [d for d in os.listdir('.')] 
# print L

# for x in L:
# 	# print x
# 	if '.py' == os.path.splitext(x)[1]:
# 		print x

# L = {'x':'A', 'y':'B', 'z':'C'}
# for k,v in L.items():
# 	print k, '=', v

# d = [k + '=' + v for k, v in L.items()]
# print d

# G = (x*x for x in range(10))
# for j in G:
# 	print j


# def fib(max):
# 	n, a, b=0,0,1
# 	while n<max:
# 		print b
# 		# print a, b
# 		a, b = b, a+b
# 		# print a, b
# 		n = n+1
# 	return 'done'

# fib(20)

def f(x, y):
	return x+y

# r = map(f, [1,2,3,4,5,6,7,8,9])
# print list(r)

# r = map(str, [1,2,3,4,5,6,7,8,9])
# print list(r)

# r = reduce(f, [1, 2, 3, 4])
# print  r

# def is_odd(n):
# 	return n%2 == 1

# L = list(filter(is_odd, [1,2,3,4,5,6,7,8]))
# print L

# def odd():
# 	print 'step 1'
# 	yield 1
# 	print 'step 2'
# 	yield 3
# 	print  'step 3'
# 	yield 5

# o = odd()
# for x in o:
# 	print x


def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n

def _not_divisible(n):
	return lambda x:x%n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 1000:
		print n
	else:
		break