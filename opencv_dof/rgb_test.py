#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: rgb_test.py
@time: 2022/9/28 14:07
@desc:
'''

import numpy as np
import cv2 as cv


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

# 创建一个黑色图像，一个窗口，然后和回调绑定
img = np.zeros((512, 512, 3), np.uint8)


j = 0
y = 0
for r in range(256):
    print(r, end=' ')
    for g in range(256, -1, -1):
        cv.circle(img, (r, y), 1, (r, g, 0), 1)

        y = int(j%255)
        print(y, ' |', end='')
        if y == 0:
            print()
        # cv.circle(img, (x, y), 1, (r, y, g), 1)
        j += 1





cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while (1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

if __name__ == '__main__':
    # j = 0
    # for i in range(10):
    #     for i in range(10):
    #         j += 1
    #         print(int(j/10), int(j%10))
    print('hello world')
