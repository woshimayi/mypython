'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: sqlite3_test.py
@time: 24/4/1 19:26
@desc: 
'''

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# 创建表
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)''')

# 插入数据
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Jane', 25))

# 提交更改
conn.commit()

# 关闭连接
conn.close()

if __name__ == '__main__':
    print('Hello world')
