#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: matplotlib_1.py.py
@time: 21/1/7 20:29
@desc: 
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
print(x, 3*np.pi)




plt.plot(x, y_sin)
plt.plot(x, y_cos)

plt.xlabel('x axis lable')
plt.ylabel('y axis lable')

plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])


plt.show()





