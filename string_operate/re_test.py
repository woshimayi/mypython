#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: re_test.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/23 20:31
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/23 20:31
 * @Descripttion: 正则表达式 练习
'''

# if __name__ == '__main__':
#     print('Hello world')

import re
'''
pattern = re.compile(r'[1-9]([0-9]{5,11})')
str = r'12345678'
print(pattern.search(str).groups())
'''

# 数字匹配
pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
pattern = re.compile(r'\d\d\d\d-\d\d-\d\d')
pattern = re.compile(r'(\d)\d\d\d\D\d\d\D\d\d')
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
pattern = re.compile(r'(\d{2,4}[-]?)+')
pattern = re.compile(r'(\d{4}[-]?)(\d{2}[-]?){2}')
pattern = re.compile(r'(\d{4}[-]?)(\d{2}[-]?){2}')
str = r'1988-05-20'
print('1', pattern.search(str))

pattern = re.compile(r'(\d{4}[-]?)(\d{2}[-]?){2}')
str = r'(1988)-05-20'
print('1', pattern.search(str))

pattern = re.compile(r'(\d{2}[-]?){4}')
str = r'88-05-20-3488'
print('2', pattern.search(str))


pattern = re.compile(r'(\d{2}[.-]?)+')
str = r'88-05-20-3434-345-567-'
print('3', pattern.search(str))


pattern = re.compile(r'(\d{2,3}[.-]?)+')
str = r'88-05-20-3434.345.567'
print('4', pattern.search(str))


# pattern = re.compile(r'^(\(\d{2}\)|^\d{2}[.-]?)?\d{3}[.-]?')
pattern = re.compile(r'^(\(\d{2}\)[.-]?)?\d{3}[.-]?\d{4}$')
str = r'(88)-345.5674'
print('5', pattern.search(str))

pattern = re.compile(r'^(\d{2}[.-]?)?\d{3}[.-]?\d{4}$')
str = r'88-345.5674'
print('6', pattern.search(str))


pattern = re.compile(r'^(\(\d{2}\)|\d{2})[.-]?\d{3}[.-]?\d{4}$')
str = r'(88)-345.5674'
print('7', pattern.search(str))
str = r'88-345.5674'
print('7', pattern.search(str))


pattern = re.compile(r'(\d{6}[,]?)+')
str = r'104007,104007,104006,104001,104006'
print('8', pattern.search(str))


pattern = re.compile(r'(^(\[(.*)]))(.*)')
str = r'[迅雷下载www.2tu.cc]航班.BD1280高清中字.rmvb'
print('9', pattern.search(str), '\t\t\t\t', pattern.search(str).groups()[-1])


pattern = re.compile(r'(.*).mp4')
str = r'[迅雷下载www.2tu.cc]航班.BD1280高清中字.rmvb'
print('10', pattern.search(str), '\t\t\t\t', pattern.search(str).groups()[-1])




