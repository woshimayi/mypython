# -*- coding: UTF-8 -*-

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%H:%M:%S', time.localtime(time.time())))