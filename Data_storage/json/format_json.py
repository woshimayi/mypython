'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: format_json.py
@time: 2024/11/08 11:54
@desc: 
'''

import json

if __name__ == '__main__':

    sJOSN =  r'c.json'
    with open(sJOSN, 'r', encoding='utf-8') as f:
        sValue = json.loads(json.dumps(json.load(f)))
        print(sValue)
        for key,val in sValue.items():
            print("%15s  :  \033[1;32m %-10s \033[0m" % (key,val))


    print('Hello world')
