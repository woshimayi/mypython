#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:20:51 2018

@author: zs
"""

import sys

#str = '112233445566'
#str1 = 'asdfghjkl'

#str = str1

#print(str)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        #print(sys.argv[1])
        str = sys.argv[1]
        #print(str)
        #str1 = append(str[0], str[1], str[2], str[3], str[4], str[5], str[6], str[7], str[8], str[9], str[10], str[11])
        
        str1 = 'write mac 1 %s%s:%s%s:%s%s:%s%s:%s%s:%s%s' % (str[0], str[1], str[2], str[3], str[4], str[5], str[6], str[7], str[8], str[9], str[10], str[11])
        print(str1)