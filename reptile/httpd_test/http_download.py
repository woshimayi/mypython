#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: http_download.py
@time: 22/11/29 15:01
@desc:
'''
import ctypes
import os
import sys
import time
from time import sleep
import requests

download_url = 'http://172.16.80.4/anysize/100k'

headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""
        }

def download(url=download_url):
    try:
        print('\t\t' + time.strftime("%Y%m%d-%H:%M:%S", time.localtime()) + '    ', end='', flush=True)
        tmp_file = r'QQ.exe'
        if os.access(tmp_file, os.F_OK):
            os.remove(tmp_file)

        r = requests.get(url, headers=headers, timeout=20, stream=True)
        size = r.headers.get('Content-Length')
        j = 1
        if 200 == r.status_code:
            print('connect download url success', url, end='', flush=True)
            with open(tmp_file, "wb") as f:
                for chunk in r.iter_content(chunk_size=512):
                    f.write(chunk)
                    print('.', end='', flush=True)

                f.close()
                print(" download success", flush=True)
        else:
            print('connect download url fail', url, flush=True)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    download("http://172.16.80.4/anysize/100k")
    print('hello world')
