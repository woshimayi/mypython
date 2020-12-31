# -*- coding: UTF-8 -*-

# 题目：利用递归方法求5!。

# 程序分析：递归公式：fn=fn_1*4!


def fact(j):
	sum = 0
	if j == 0:
		sum = 1
	else:
		# print(sum)
		sum = j * fact(j-1)
	return sum

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))