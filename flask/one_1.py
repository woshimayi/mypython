#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: one_1.py
@time: 23/5/9 17:53
@desc:
'''

from flask import Flask, url_for, request, redirect
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('./static/commit_html.html')


@app.route('/index.html')
def index():
    return '<h1>index</h1>\n <h1>Welcome to gerrit log commit</h1>'

@app.route('/index.html/')
def _index():
    return 'index !--'

# @app.route('/<number>')
# @app.route('/<int:number>')
# def index_num(number=None):
#     return 'index- %s !' % number

@app.route('/<hashnum>')
def index_hash(hashnum=None):
    count = 0
    flag = 0
    f = open(r'commit.txt', "r")
    for line in f.readlines():
        # print(line)
        if hashnum == line.strip():
            print("第 "+str(count)+" 行已找到.")
            print("该行内容: \n"+line)
            flag = True
            break
        count += 1
    f.close()
    if flag:
        return str(count)
    else:
        return  str(-1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.methods == 'GET':
        print("login GET")
    else:
        print("login POST")
    return 'login: !'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8056, debug=True)
    app.config["timeout"] = 2
    with app.test_request_context():
        print(url_for('index.html', next='/'))
        url_for('static', filename='style.css')