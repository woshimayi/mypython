# -*- coding: UTF-8 -*-


# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 程序分析：学会分解出每一位数。

j = 0
n = 12345
a= 0
while n != 0:
	a = n%10
	print(a, end=' ')
	n = int(n/10)
	# print(n)
	j += 1
	print()


print('j = %d'%j)