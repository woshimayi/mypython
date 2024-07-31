'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: flask_test.py
@time: 24/4/1 19:27
@desc: 
'''
import sqlite3

from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

@app.route('/index.html')
def index():
    return '<h1>Welcome to gerrit log commit</h1>'


@app.route('/')
@app.route('/gitid/')
def result():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute a query to fetch all users
    # cursor.execute('SELECT * FROM users ')                # 正序显示
    cursor.execute('SELECT * FROM users ORDER BY id DESC')  # 倒叙显示
    users = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Pass the user data to the template
    return render_template('result.html', users=users)


@app.route('/branch/<branchName>')
def branch(branchName=None):
    print("zzzzz", branchName)
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute a query to fetch all users
    # cursor.execute('SELECT * FROM users ')                # 正序显示
    cursor.execute('SELECT * FROM users WHERE branch == ? ORDER BY id DESC', (branchName,))  # 倒叙显示
    users = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Pass the user data to the template
    return render_template('result.html', users=users)



@app.route('/<hashnum>')
def index_hash(hashnum=None):
    print(hashnum)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        ret = conn.execute("SELECT id,commitid FROM users WHERE commitid == ?", (hashnum,))
        if ret:
            print(ret)
            result = ret.fetchone()
            print(result[0]-1, result[1])
            conn.close()
            return str(result[0]-1)
    except:
        return str(-1)

@app.route('/gitid/<gitid>')
def index_gitid(gitid=None):
    print(gitid)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        ret = conn.execute("SELECT id,commitid FROM users WHERE id == ?", (int(gitid)+1,))
        print(ret)
        if ret:
            result = ret.fetchone()
            print(result[0]-1, result[1])
            conn.close()
            return str(result[1])
    except:
        return str(-1)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8058, debug=True)