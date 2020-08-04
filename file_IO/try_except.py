# -*- coding: utf-8 -*-
import os, sys


e = 100

# try:
# 	fh = open('testfile', 'r')
# 	# fh.write("1234567890")
# 	print(fh.read())
# except IOError:
# 	print("write fail")
# else:
# 	print("write success")
# 	fh.close()
# finally:
# 	print("123456")

def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

try:
    mye(0)
except "Invalid level!":
    print(1)
else:
    print(2)