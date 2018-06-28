# -*- coding: UTF-8 -*-


import sys

def PP(*a):
    print('['+sys._getframe().f_code.co_filename+']'+'['+sys._getframe(1).f_code.co_name+']'+'['+':',sys._getframe().f_back.f_lineno,']',)
    for e in a:
    	# print namestr(e, locals())
    	print('['+e.__class__.__name__, e,']',)
    print


def reduceNum(n):
	print(n)
	if not isinstance(n, int) or n <= 0:
		print('input!')
		exit(0)
	elif n in [1]:  #判断你是否等于1
		print(n)
	while n != 1:
		for index in range(2, n+1):
			if n % index == 0:
				n = int(n/index)
				if n == 1:
					print(index)
				else:
					print(index,'*', end="")
				break

reduceNum(90)
reduceNum(100)