#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: test_dof.py
@time: 2021/2/22 15:37
@desc: ini file read write
'''


import configparser


# write ini file
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']

topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes'


with open('example.ini', 'w') as configfile:
    config.write(configfile)

# read ini file
config = configparser.ConfigParser()

print('sections')
print('1', config.sections())
print('2', config.read('example.ini'))
print('3', config.sections())
print('4', ('bitbucket.org' in config))
print('5', ('bytebong.com' in config))
print('6', config['bitbucket.org']['User'])
print('7', config['DEFAULT']['Compression'])

topsecret = config['topsecret.server.com']
print('8', topsecret['ForwardX11'])
print('9', topsecret['Port'])

for key in config['bitbucket.org']:
    print('10', key)

for key in config['topsecret.server.com']:
    print('12', key, config['topsecret.server.com'][key])

print('11', config['bitbucket.org']['ForwardX11'])

# -sections得到所有的section，并以列表的形式返回
print('sections:', ' ', config.sections())

# -options(section)得到该section的所有option
print('options:', ' ', config.options('bitbucket.org'))

# -items（section）得到该section的所有键值对
print('items:', ' ', config.items('bitbucket.org'))

# -get(section,option)得到section中option的值，返回为string类型
print('get:', ' ', config.get('bitbucket.org', 'user'))

# 首先得到配置文件的所有分组，然后根据分组逐一展示所有
for sections in config.sections():
    for items in config.items(sections):
        print(items, items[0], items[1])

# add section
config = configparser.ConfigParser()

config.add_section('type')
config.set('type', 'stun', 'bool')

with open('example.ini', 'a') as configfile:
    config.write(configfile)

# remove section option
config = configparser.ConfigParser()
print('2', config.read('example.ini'))
# config.remove_option('bitbucket.org', 'user')
# config.remove_section('bitbucket.org')

config.write(open('example.ini', 'w'))