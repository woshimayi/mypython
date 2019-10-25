import re


# *代表任意前面的元素
import os
import sys
from fnmatch import fnmatch, fnmatchcase

line = 'asdf fjdk; afed, fjek,asdf, foo'
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

filename = 'http://www.baidu.com'
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


text1 = '11/23/2012'

# print(re.match(r'\d+/\d+/\d+', text1))

datepat = re.compile(r'\d+/\d+/\d+')
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

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$') # 捕获分组以便分别将每个组的内容提取出来
print(datepat.match('11/27/2012sdfsd'))
print(datepat.match('11/27/2012'))