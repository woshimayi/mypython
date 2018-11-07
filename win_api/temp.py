# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar)')
cursor.execute('insert into user (id,name) values (\'1\', \'Michael\')')
cursor.rowcount

print('1111111111')

cursor.execute('select * from user where id = ? ',('1'))
value =cursor.fetchall()

print(value)



















cursor.close()
conn.commit()
conn.close()