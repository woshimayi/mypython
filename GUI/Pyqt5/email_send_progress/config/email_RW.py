#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: email_RW.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/20 17:18
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/20 17:18
 * @Descripttion: 
'''
import configparser

'''
# write ini file
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']

topsecret['Port'] = '50022'  # mutates the parser
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
'''


class Email_operate(object):
    """docstring for Email_operate"""

    def __init__(self, file=r'email.ini'):
        print("open conf file: ", file)
        super(Email_operate, self).__init__()
        self.file = file

        self.config = configparser.ConfigParser()
        err = self.config.read(self.file)
        print("err = ", err)
        if 0 == len(err):
            print("err = ssss")
            self.config['Global'] = {}
            self.config['send'] = {'mail': '',
                                   'user': '',
                                   'password': ''}
            self.config['recv'] = {'user': ''}

            with open(self.file, 'w') as configfile:
                self.config.write(configfile)

    def read(self, section, key):
        try:
            if section in self.config:
                return self.config[section][key]
        except:
            pass

    def write(self, section, key, value):
        try:
            if section in self.config:
                self.config[section][key] = value
            else:
                self.config.add_section[section]
                self.config.set(section, key, value)

            with open(self.file, 'w') as configfile:
                self.config.write(configfile)
        except:
            pass

    def show(self):
        for sections in self.config.sections():
            print("[%s]" % sections)
            for items in self.config.items(sections):
                print("%s = %s" % (items[0], items[1]))
            print()

    def read_sendMail(self):
        return self.read("send", "mail")
        pass

    def read_sendUser(self):
        return self.read("send", "user")
        pass

    def read_sendPass(self):
        return self.read("send", "password")
        pass

    def read_recvMail(self):
        return self.read("recv", "mail")
        pass

    def read_recvUser(self):
        return self.read("recv", "user")
        pass

    def write_mail(self):
        pass

    def write_user(self):
        pass

    def write_pass(self):
        pass

    def __del__(self):
        print("end ... ")


if __name__ == '__main__':
    print('Hello world')
    C = Email_operate("email.ini")
    C.show()
    print("user = zzz", C.read("send", "user"))
    C.write("recv", "pass", "ssssss")
    C.show()
