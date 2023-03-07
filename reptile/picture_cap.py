#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: picture_cap.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/8/23 19:47
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/23 19:47
 * @Descripttion:  定期截指定屏幕
'''
import time

from PIL import ImageGrab

if __name__ == '__main__':

    num = 0
    while True:
        try:
            print('begain', end='')
            ss_region = (1337, 778, 1833, 1041)  # 距离左上右下的像素
            ss_img = ImageGrab.grab(ss_region)
            log_file = time.strftime("%Y%m%d", time.localtime()) + str(num) + '.jpg'
            ss_img.save(log_file)
            num = num + 1
            print('    end')
            time.sleep(3)
        except Exception as e:
            print(e)



    print('Hello world')
