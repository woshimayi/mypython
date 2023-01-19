#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: plt_2.py
@time: 21/1/7 20:35
@desc: 
'''


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(4, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(4, 1, 2)
plt.plot(x, 2*y_sin)
plt.title('Sine')

plt.subplot(4, 1, 3)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.subplot(4, 1, 4)
plt.plot(x, 4*y_cos)
plt.title('Cosine')

plt.show()