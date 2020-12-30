#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: key_digital.py
@time: 20/12/30 20:28
@desc: 
'''
import keyboard





# keyboard.press_and_release('shift+s, space')
#
# keyboard.write('The quick brown fox jumps over the lazy dog.')
#
# keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
#
# # Press PAGE UP then PAGE DOWN to type "foobar".
# keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
#
# # Blocks until you press esc.
# keyboard.wait('esc')
#
# # Record events until 'esc' is pressed.
# recorded = keyboard.record(until='esc')
# # Then replay back at three times the speed.
# keyboard.play(recorded, speed_factor=3)
#
# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')
#
# # Block forever, like `while True`.
# keyboard.wait()
import pyperclip


def test_a():
    print('aaa')

def test(x):
    a = pyperclip.paste()
    print('a ', a)
    print(x)

if __name__ == '__main__':
    keyboard.add_hotkey('f1', test_a)
    #按f1输出aaa
    keyboard.add_hotkey('ctrl+c', test, args=('b',))
    #按ctrl+alt输出b
    keyboard.wait()
    #wait里也可以设置按键，说明当按到该键时结束