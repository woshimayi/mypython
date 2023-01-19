#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: create_save.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/8/8 18:29
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/8/8 18:29
 * @Descripttion: 
'''

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
print(cap)

# 声明编码器和创建 VideoWrite 对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
print(fourcc)

out = cv.VideoWriter('output.avi',fourcc, 20.0, (1920,1080))
print(out)

while(cap.isOpened()):
    ret, frame = cap.read()
    print(ret)
    if ret==True:
        frame = cv.flip(frame,0)
        print(frame)
        # 写入已经翻转好的帧
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放已经完成的工作
cap.release()
out.release()
cv.destroyAllWindows()