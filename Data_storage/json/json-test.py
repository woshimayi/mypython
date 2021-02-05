#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: json-test.py
@time: 2020/8/11 21:11
@desc:
'''
import logging
import pandas as pd
import json
import os

'''
# Python 对象（字典）：
x = {
  "name": "Bill",
  "age": 63,
  "city": "Seatle"
}

# 转换为 JSON：
y = json.dumps(x)

# 结果是 JSON 字符串：
print(y)


# 一些 JSON:
x =  '{ "name":"Bill", "age":63, "city":"Seatle"}'

# 解析 x:
y = json.loads(x)

# 结果是 Python 字典：
print(y["age"])
'''

# 读取json 文件为字符串
def json_read(file):
    with open(file, 'r') as f:
        return json.load(f)


def json_find(file, key):
    if os.access(file, os.F_OK):
        with open(file, 'r') as f:
            dict = json.load(f)
            # print('dict', dict)
            for key1, value in dict.items():
                # print('key:%s, value:%s' % (key1, value))
                for key1, value1 in value.items():
                    print('%s, %s' % (key1, value1))
    else:
        print('file not access')


# 格式化json 字符写到到文件中
def json_write(file, key, value):
    # with open(file, 'r') as f:
    #     data = json.load(f)

    with open("c.json", 'w') as f:
        data1 = json.dumps(
            [{key: value}],
            ensure_ascii=False,
            indent=4,
            separators=(
                ',',
                ':'))
        # json.dump(data4, f)
        f.write(data1)


# json_find('c.json', 'description')
# print('ssss', data['Region End']['description'])
#
json_write('c.json', 'description', 'Folding Region End asd')
json_write('c.json', '111', '222')
data = json_read('c.json')
print('data', data)


# date = [
#   {"auto": "123"}, {"man": "456"}
# ]

# print(date[0]['auto'])
#

# for i in range(10, 0, -1):
# 	print(i)

# #!coding=utf-8
# import logging

# # 开始使用log功能
# logging.info('这是 loggging info message')
# logging.debug('这是 loggging debug message')
# logging.warning('这是 loggging a warning message')
# logging.error('这是 an loggging error message')
# logging.critical('这是 loggging critical message')


# '''
#!coding=utf-8

# 设置logging的等级以及打印格式
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(funcName)s:line:%(lineno)d] - %(levelname)s: %(message)s')

a = 'sss'
b = 'vvv'


# 开始使用log功能
logging.debug(a)
logging.info('%s %s ' % (a, b))
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')


# '''


# def analysis(file, user_id):
#     with open(file, 'r') as f:
#         if not f:
#             return 0
#         df = pd.read_json(f, orient='records')
#         print(df)
#         # print(df['Region Start']['body'])
#         # df['Region Start']['body'] = '#pragma region $9'
#         # print(df['Region Start']['body'])
#         # dfs = df[df['description'] == ]
#         # times = dfs.shape[0]
#         # minutes = dfs['prefix'].sum()
#
#     # return times, minutes
#
#
# if __name__ == '__main__':
#     result = analysis('c.json', 199071)
#     print(result)
