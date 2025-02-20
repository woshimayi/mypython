#!/usr/bin/env python
# -*- coding:utf-8 -*-

#####################################################
# ghtoc   : a markdown toc generator
# Author  : Kai Yuan <kent.yuan@gmail.com>
# Usage   : toc.py <markdown file>
# Date    : 2014-12-02
# License :
#Copyright (C) 2014 Kai Yuan
#
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the "Software"),
#to deal in the Software without restriction, including without limitation
#the rights to use, copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included
#in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#####################################################

import re
import sys
import shutil,datetime

top_level=77
lnk_temp='%s- [%s](#%s)'
TOC='#### Table of contents'
REF='(toc generated by [ghtoc](https://github.com/sk1418/ghtoc))'

def generate_toc(fname):
    global top_level
    lines = []
    with open(fname, 'r') as file:
        lines = file.readlines()
    ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    destf= '.'.join((fname,ts,'bak'))
    shutil.copy(fname, destf)
    print("Backup was created: [%s]"%destf)
    headers = [e.rstrip() for e in lines if re.match(r'#+', e)]
    #find top_level
    for i,h in enumerate(headers):
        ln = len(re.search(r'^#+',h).group(0))
        top_level = ln if ln < top_level else top_level
        headers[i] = re.sub(r'^#+\s*', str(ln)+' ', h)
    headers = [tr_header(h) for h in headers]
    with open(fname,'w') as f:
        f.write(TOC+'\n')
        f.write(REF+'\n')
        f.write('\n'.join(headers) + '\n')
        f.write(''.join(lines) + '\n')
        f.write('\n\n')


def tr_header(header):
    global lnk_temp
    lvl, txt = re.findall(r'^(\d+) (.*)', header)[0]
    # return lnk_temp%((int(lvl)-top_level)*'    ', txt, re.sub(' ','-',re.sub('[^-a-z0-9 ]','',txt.lower())))
    return lnk_temp%((int(lvl)-top_level)*'    ', txt, re.sub(' ','-',txt))

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("""
            Usage:
            toc.py <markdown file>
        """)
    else:
        infile = sys.argv[1]
        generate_toc(infile)
