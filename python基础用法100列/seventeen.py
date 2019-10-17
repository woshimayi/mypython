# -*- coding: UTF-8 -*-

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string

s = input('please input :\n')

letters = 0
space = 0
digit = 0
other = 0

i = 0

while i < len(s):
	c = s[i]
	i += 1
	if c.isalpha():
		letters  += 1
	elif c.isspace():
		space += 1
	elif c.isdigit():
		digit += 1
	else:
		other += 1
print('letters=%d, space=%d, digit=%d, other=%d' % (letters, space, digit, other))

