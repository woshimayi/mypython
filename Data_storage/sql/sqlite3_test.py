'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: sqlite3_test.py
@time: 23/7/12 20:05
@desc: 
'''

import sqlite3

# 链接数据库，若数据库不存在则创建
con = sqlite3.connect(r"123.db")

# 在内存中创建数据库
# con = sqlite3.connect(":memory:")

# 创建游标对象
cur = con.cursor()

# 新建表abc，包含id，name，age三列，sqlite可以省略类型,ID为主键（主键不能重复）并且不能为空，若已有该表则报错
# cur.execute("CREATE TABLE commit(id TEXT PRIMARY KEY NOT NULL,name TEXT,age INT)")

# 新建表xyz，若已有该表则忽略，
# cur.execute("CREATE TABLE IF NOT EXISTS xyz(id TEXT PRIMARY KEY NOT NULL,name TEXT,age INT)")

# 删除表xyz
# cur.execute("DROP TABLE xyz")

# 修改已有表名称，abc>>mytable
# cur.execute("ALTER TABLE abc RENAME TO mytable")

# 在已有表中添加列abc,字段类型为text，若已有该列则报错
# cur.execute("ALTER TABLE mytable ADD abc TEXT")

# 修改已有列的列名称：看文档应该是这么写但一直报错，可能是python api 中 alter方法并不支持重命名列
# con.execute("ALTER TABLE mytable RENAME COLUMN abc TO sex")

# 在表mytable中插入一条记录,两种方法，一般用第二种方法，较为安全
# cur.execute("INSERT INTO mytable (id,name) VALUES ('0','狗蛋')")
cur.execute("INSERT INTO mytable(id,name) VALUES(?,?)",("1","张三丰"))

# 在表mytable中插入一条记录，若存在即忽略
cur.execute("INSERT OR IGNORE INTO mytable (id,name) VALUES ('0','狗蛋')")

# 在表mytable中插入多条记录
# info = [("2","张无忌"),("3","谢逊"),("4","令狐冲")]
# cur.executemany("INSERT INTO mytable(id,name) VALUES(?,?)",info)

# 对 seq_of_parameters 中的所有参数或映射执行一个 SQL 命令。
# cur.executemany(sql, seq_of_parameters)

# 执行多个 SQL 语句。它首先执行 COMMIT 语句，然后执行作为参数传入的 SQL 脚本。所有的 SQL 语句应该用分号（;）分隔。
# cur.executescript(sql_script)

# 查询数据
cur.execute("SELECT id,name FROM mytable")
cur.execute("SELECT * FROM mytable")

# 获取查询结果集中所有（剩余）的行，返回一个列表
print(cur.fetchall())

# 修改记录，在id为3的记录中将该条记录的name字段内容修改为金毛狮王
# cur.execute("UPDATE mytable SET name = ? where id = ?",("金毛狮王","3"))

# 修改一条记录多个字段，在id为3的记录中将该条记录的name字段内容修改为金毛狮王，age改为44
# cur.execute("UPDATE mytable SET name = ?,age = ? where id = ?",("金毛狮王",44,"3"))

# 删除整条记录
# n = cur.execute("delete from mytable where id=?",("1",)) #逗号不能省，元组元素只有一个的时候一定要加逗号
# print("删除{num}行记录".format(num = n.rowcount))

# 事务提交，保存修改内容。
con.commit()

# 事务回滚，数据库回到上次提交保存的状态。
# con.rollback()

# 数据库关闭，不自动提交保存。如果在关闭数据库连接之前没有调用 commit()，那么你的修改将会丢失！
con.close()


if __name__ == '__main__':
    print('Hello world')
