# -*- coding: UTF-8 -*-

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# 程序分析：请抓住分子与分母的变化规律。

# a = 2
# b = 1
# s = 0

# for n in range(1, 21):
# 	s += a/b

# 	t = a
# 	a = a+b
# 	b = t
# print(s)
# ==============================================

from functools import reduce
a = 2
b = 1
l = []

for n in range(1,21):
	b, a = a, a+b
	l.append(a/b)
# print(l)
print(reduce(lambda x,y: x+y, l))

print(reduce(lambda x,y: x*y, [1,2,3,4]))
print(reduce(lambda x,y: x+y, [1,2,3,4]))