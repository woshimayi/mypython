#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: batch.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/23 17:39
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/23 17:39
 * @Descripttion: 
'''

import re

import xlwt


class Batch(object):
    """docstring for Batch"""

    def __init__(self):
        super(Batch, self).__init__()
        # self.arg = arg
        self.workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.sheet = self.workbook.add_sheet('test', cell_overwrite_ok=True)

    def match_string(self):
        i = 0;
        with open("vlan_api.c", 'r') as f:
            for line in f.readlines():
                # print("zzzzz", line.strip().split(')|('))
                m = re.search(r'^*\d\$', line.strip())
                # print('mmmmm', m.string.split('    '))
                print('mmmmm', m.groups())
                L = m.string.split('    ')
                i = i + 1
                print(i)
                # print(re.search(r'^\*d\(*$', L[0]).groups())
                # self.write_excl(i, m.string.split('    ')[0], m.string.split('    ')[1].split(' ', 1)[1:])
            # self.workbook.save(r'./test.xls')

    def write_excl(self, num, x1, x2):
        self.sheet.write(num, 0, x1)
        self.sheet.write(num, 1, x2)

    def __del__(self):
        self.workbook.save(r'./test.xls')



if __name__ == '__main__':
    print('Hello world')
    B = Batch()
    B.match_string()
