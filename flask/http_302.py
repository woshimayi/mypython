'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: http_302.py
@time: 2025/11/25 13:54
@desc: 
'''

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/302-test')
def handle_302():
    # 返回 302 Found 状态码，并重定向到目标地址
    # 目标地址可以是任何您想测试的 URL
    return redirect("http://172.16.27.192:8080/123", code=302)


@app.route('/speedtest/', defaults={'subpath': ''})
@app.route('/speedtest/<path:subpath>')
def handle_speedtest(subpath):
    # 返回 302 Found 状态码，并重定向到目标地址
    # 目标地址可以是任何您想测试的 URL
    return redirect("http://172.16.27.192:8080/123", code=302)

if __name__ == '__main__':
    # 运行服务器
    print("运行在 http://172.16.27.192")
    app.run(host="0.0.0.0", port=80, debug=True)