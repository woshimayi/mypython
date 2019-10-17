# -*- coding: UTF-8 -*-

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

score =  int(input('input score:'))

while score > 0:
	if score >= 90:
		print('Á')
	elif 80 <= score < 90:
		print('B')
	elif 70 <= score < 80:
		print('C')
	elif score < 70:
		print('D')
	elif score == 0:
		break
	score =  int(input('input score:'))
