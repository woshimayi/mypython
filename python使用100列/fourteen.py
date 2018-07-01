# -*- coding: UTF-8 -*-


# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# 程序分析：对n进行分解质因数，应先找到一个最小的质数index，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被index整除，则应打印出index的值，并用n除以index的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


# def reduceNum(n):

#     print('{}'.format(n),)
#     if not isinstance(n, int) or n <= 0:
#         print('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :         # 等同于你==1
#         print('{}'.format(n))

#     while n not in [1] : # 循环保证递归  等同于  n != 1
#         for index in range(2, n + 1) :
#             print('n = %d index = %d' %(n, index))
#             if n%index == 0:
#                 n = int(n/index) # n 等于 n/index  除
#                 print('n = %d index = %d' %(n, index))
#                 if n == 1:    #等于n
#                     print('index = %d' %index)
#                 else : # index 一定是素数
#                     print('{} *'.format(index),)
#                 break
# reduceNum(90)

# =========================================================================


def reduceNum(n):
	print('{}'.format(n))
	if n <= 0 and isinstance(n, int):
		print('plese  input interger')
		exit(0)
	elif n == 1:
		print('{}'.format(n))

	while n != 1:
		for index in range(2, n+1):
			if n%index == 0:
				n = int(n/index)
				# print(n)
				if n == 1:
					print(index)
				else:
					print(index,end=' ')



reduceNum(90)

# ==============================================================================

l = [] 
n = 90
while n>1:
	for i in range(2, n+1):
		if n%i == 0:
			n = int(n/i)
			l.append(str(i))
			break

print(l)
