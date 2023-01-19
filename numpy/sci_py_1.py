#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: sci_py_1.py
@time: 21/1/7 20:24
@desc: 
'''

from scipy.misc import imread, imsave, imresize

img = imread('img.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1, 0.95, 0.9]

img_tinted = imresize(img_tinted, (300, 300))

imsave('123.jpg', img_tinted)