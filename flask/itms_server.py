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

from flask import Flask, url_for, request, redirect, send_from_directory, Response, make_response
from flask import render_template
from flask import Flask, flash
from werkzeug.utils import secure_filename
import os
from pathlib import Path

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bin'}


@app.route('/index.html')
@app.route('/')
def index():
    return '<h1>index</h1>\n <h1>Welcome to gerrit log commit</h1>'


@app.route('/index.html/')
def _index():
    return 'index !--'


# @app.route('/<number>')
# @app.route('/<int:number>')
# def index_num(number=None):
#     return 'index- %s !' % number

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.methods == 'GET':
        print("login GET")
    else:
        print("login POST")
    return 'login: !'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST', 'PUT'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        print(file)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            print(filename, os.path.join('uploads', filename))
            file.save(os.path.join('uploads', filename))
    elif request.method == 'PUT':
        data = request.get_data(as_text=True)
        f = open('123', 'wb', code='utf-8')
        print('2')
        f.write(data)
        print('123', '保存成功')
        f.close()
        # print('zzzzz', request.files)
        # file = request.files['file']
        # print(file, file.filename)
        # if file:
        #     filename = secure_filename(file.filename)
        #     print(filename, os.path.join('uploads', filename))
        #     file.save(os.path.join('uploads', filename))

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/<path>', methods=['GET'])
def download_file(path):
    base_dir = os.path.dirname(__file__)
    resp = make_response(open(os.path.join(base_dir, path)).read())
    resp.headers["Content-type"]="application/json;charset=UTF-8"
    return resp


@app.route('/downloadfile/<fullfilename>', methods=['GET', 'POST'])
def downloadfile(fullfilename):
    if request.method == 'GET':
        # fullfilename = request.args.get('filename')

        fullfilenamelist = fullfilename.split('/')
        filename = fullfilenamelist[-1]
        filepath = fullfilename.replace('static/%s' % filename, '')

        # 普通下载
        # response = make_response(send_from_directory(filepath, filename, as_attachment=True))
        # response.headers["Content-Disposition"] = "attachment; filename={}".format(filepath.encode().decode('latin-1'))
        # return send_from_directory(filepath, filename, as_attachment=True)
        # 流式读取
        def send_file():
            store_path = fullfilename
            with open(store_path, 'rb') as targetfile:
                while 1:
                    data = targetfile.read(20 * 1024 * 1024)  # 每次读取20M
                    if not data:
                        break
                    yield data

        response = Response(send_file(), content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % filename  # 如果不加上这行代码，导致下图的问题
        return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8056, debug=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
