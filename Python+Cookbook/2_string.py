import json
import re
import requests

# *代表任意前面的元素
import os
import sys
from fnmatch import fnmatch, fnmatchcase


# line = 'asdf fjdk; afed, fjek,asdf, foo'
# print(re.split(r'[;]', line))
# print(re.split(r'[,]', line))
# print(re.split(r'[ ]', line))
# print(re.split(r'[ ]', line))
# print(re.split(r'[\s,;]', line))  # \s 空格
#
# print(re.split(r'[\s]', line))
# print(re.split(r'[f]', line))
# print(re.split(r',|;', line))
# print(re.split(r'[,;]', line))
# print(re.split(r'[,|;]', line))
# print(re.split(r'(?:\s)', line))

# filename = 'http://www.baidu.com'
# print(filename.endswith('.com'))
# print(filename.startswith('http://'))


# filenames = os.listdir('../test')
# print(filenames, len(filenames))
#
# filenames = [name for name in filenames if name.endswith('.py')]
# filenames = [name for name in filenames if name.endswith(['.py', '.db'])]
# print(filenames, len(filenames))

# print(re.match('http:|https:|ftp:', filename))


# print(fnmatch(filename, 'HTTP*'))    # 不区分大小写
# print(fnmatchcase('foo.txt', '*txt'))  # 区分大小写

# addresses = [
#     '5412 N CLARK ST',
#     '1060 W ADDISON ST',
#     '1039 W GRANVILLE AVE',
#     '2122 N CLARK ST',
#     '4802 N BROADWAY',
# ]

# addr = [addr for addr in addresses if fnmatchcase(addr, '*ST')]
# print(addr)
#
# addr = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9]*ST')]
# print(addr)


# text1 = '11/23/2012'

# print(re.match(r'\d+/\d+/\d+', text1))

# datepat = re.compile(r'\d+/\d+/\d+')
# print(datepat.findall(text1))

# datepat = re.compile(r'(\d+)/(\d+)/(\d+)') # 捕获分组以便分别将每个组的内容提取出来
# m = datepat.match('11/12/2012')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# print(m.group())
# print(m.groups())

# month, day, year = m.groups()
# print(month, day, year)
# print(datepat.findall(text1))
# for month, day, year in datepat.findall(text1):
#     print('{}-{}-{}'.format(year, month, day))

# datepat = re.compile(r'(\d+)/(\d+)/(\d+)$') # 捕获分组以便分别将每个组的内容提取出来
# print(datepat.match('11/27/2012sdfsd'))
# print(datepat.match('11/27/2012'))
# m = datepat.match('11/27/2012')
# print(m.group())
# print(m.groups())
# print(re.findall(r'(\d+)/(\d+)/(\d+)', text1))

# text = 'yeah, but no, but yeah, but no, but yeah'
# print(text.replace('yeah', 'yekk'))
# print(text)
# print(text.replace('yeah', 'yess'))

# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
#
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')  # 预先编译以提高性能
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')  # 预先编译以提高性能
# print(datepat.sub(r'\3-\1-\2', text))

from calendar import month_abbr
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return ('{} {} {}'.format(m.group(3), mon_name, m.group(2)))
#
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')  # 预先编译以提高性能
# print(datepat.sub(change_date, text))
#
# datepat = re.compile(r'^(\d+)/(\d+)/(\d+)')  # 预先编译以提高性能
# print(datepat.sub(change_date, text))


# newtext, n = datepat.subn(r'\3-\1-\2', text)
# print(newtext, n)

def matchcase(word):
    def replace(m):
        text = m.group()
        # print(text)
        if text.isupper():
            print(word.upper())
            return word.upper()
        elif text.islower():
            print(word.lower())
            return word.lower()
        elif text[0].isupper():
            print(word.capitalize())
            return word.capitalize()
        else:
            return word
    return replace

text = 'UPPER PYTHON, lower python, Mixed Python'
# print(text)
# print(re.findall('python', text, flags=re.IGNORECASE))  # 忽略大小写
# print(re.sub('python', "snake", text, flags=re.IGNORECASE))  # 忽略大小写
print(re.sub('python', matchcase("snake"), text, flags=re.IGNORECASE))  # 忽略大小写

# test1 = 'UPPER PYTHON, lower python, Mixed Python'
# print(test1.islower())
# print(test1.lower())




