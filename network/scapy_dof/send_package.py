#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: send_package.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/8/15 16:47
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/15 16:47
 * @Descripttion: 
'''
import argparse

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    # group = parser.add_mutually_exclusive_group()

    parser.add_argument("-v", "--version", action="store_true", default=0, help="otuput version info")
    parser.add_argument("url", type=str, nargs="?", help="input the url")
    parser.add_argument("-o", "--output", help="otuput specify dirctory")
    parser.add_argument("-f", "--file", help="Get the url in file")
    parser.add_argument("-b", "--bing", action="store_true", help="Get the url in file")

    # 添加到参数列表中
    args = parser.parse_args()


    if args.output:
        directory = args.output
        print(directory)
    elif args.file:
        file = args.file
        print(file)
    elif args.bing:
        print(args.bing)
    elif args.version:
        print(args.version)
    else:
        print("not args")

    print('Hello world')
