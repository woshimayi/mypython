#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: key_board_get.py
@time: 20/12/30 20:04
@desc: python 键盘鼠标监听
'''


import keyboard

'''
# print(0)
# keyboard.wait('a')
# # 在按下a之前后面的语句都不会执行，下面同理
# print(1)
# keyboard.wait('b')
# print(2)
# keyboard.wait('c')
# print(3)
# keyboard.wait()
'''

'''  组合键
def test_a():
    print('aaa')

def test(x):
    print(x)

if __name__ == '__main__':
    keyboard.add_hotkey('f1', test_a)
    #按f1输出aaa
    keyboard.add_hotkey('ctrl+alt', test, args=('b',))
    #按ctrl+alt输出b
    keyboard.wait()
    #wait里也可以设置按键，说明当按到该键时结束
'''

''' 记录键盘事件
keyboard.add_hotkey('ctrl', print, args=('aaa',))
keyboard.add_hotkey('alt', print, args=('bbb',))

recorded = keyboard.record(until='esc')
#当按下esc时结束按键监听，并输出所有按键事件
print(recorded)
'''

'''  hook
def abc(x):
    print(x)
    print("111")

keyboard.hook(abc)
#按下任何按键时，都会调用abc，其中一定会传一个值，就是键盘事件
keyboard.wait()
'''

# '''
def abc(x):
    a = keyboard.KeyboardEvent('down', 28, 'enter')
    #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
    #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
    if x.event_type == 'down' and x.name == a.name:
        print("你按下了enter键")
    #当监听的事件为enter键，且是按下的时候

keyboard.hook(abc)
# keyboard.hook_key('enter', bcd)
# recorded = keyboard.record(until='esc')
keyboard.wait()
# '''

import pyautogui as pag    #监听鼠标

'''
x1, y1 = pag.position()
#输出鼠标当前位置
print(x1, y1)
'''

'''
pag.click(button='right')
#点击鼠标右键
pag.click(100, 100)
#要在指定位置点击左键
'''



