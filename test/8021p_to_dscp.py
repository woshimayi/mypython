#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: 8021p_to_dscp.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/3/22 14:36
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/3/22 14:36
 * @Descripttion: 
'''


for p in range(8):
    # print(p)
    print("input pbit:%d out dscp: %d",  (p, hex((0 & ~(0x3F << 5)) | (p << 5))))
    # print("dscp", hex((0 & ~(0x3F << 5)) | ((p & 0x07 | 0x08) << 5)))