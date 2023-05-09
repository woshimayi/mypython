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

from flask import Flask, url_for, request
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index.html')
def index():
    return 'index !'

@app.route('/index.html/')
def _index():
    return 'index !--'

@app.route('/<number>')
@app.route('/<int:number>')
def index_num(number=None):
    return 'index- %s !' % number

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
    app.run(debug=True)

    with app.test_request_context():
        print(url_for('index.html', next='/'))
        url_for('static', filename='style.css')