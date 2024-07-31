# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: sqlite_parse.py
@time: 2024/07/04 11:21
@desc: git log parse
'''
import os
import sqlite3


'''
git log --all -n 100 --pretty=format:"%H 0A %an 0A %aI 0A %s 0A %S" > gitlog.txt
'''

class Gitlog(object):
    """docstring for Gitlog"""

    def __init__(self, arg):
        super(Gitlog, self).__init__()
        self.fileDb = arg

        self.conn = sqlite3.connect(self.fileDb)
        self.c = self.conn.cursor()
        self.init()

    def init(self):
        # if not os.path.exists('database.db'):
        # 创建表
        self.c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, commitid TEXT, name TEXT, date TEXT,desc TEXT, branch TEXT)")
        pass

    def add(self, commit, name, date, desc, branch):
        self.c.execute("INSERT INTO users (commitid, name, date, desc, branch) VALUES (?, ?, ?, ?, ?)",
                       (commit, name, date, desc, branch))
        pass

    def delete(self):
        pass

    def set(self):
        pass

    def get(self):
        pass

    def search_commitExist(self, commit):
        print(commit)
        try:
            ret = self.conn.execute("SELECT id,commitid FROM users WHERE commitid == ?", (commit,))
            if ret:
                print(ret)
                result = ret.fetchone()
                print(result[0]-1, result[1])
        except:
            return -1

        return result[0]-1

    def search_commitToId(self, commit):
        print(commit)
        try:
            ret = self.conn.execute("SELECT id,commitid FROM users WHERE commitid == ?", (commit,))
            if ret:
                print(ret)
                result = ret.fetchone()
                print(result[0]-1, result[1])
        except:
            return -1

        return result[0]-1

    def search_idToCommit(self, id):
        print(id)
        try:
            ret = self.conn.execute("SELECT id,commitid FROM users WHERE id == ?", (id+1,))
            print(ret)
            if ret:
                result = ret.fetchone()
                print(result[0]-1, result[1])
        except:
            return -1

        return result[1]

    def commit(self):
        self.conn.commit()
        pass

    def close(self):
        self.conn.close()
        pass

    def gendatebase(self):
        with open(r'gitlog.txt', 'r', encoding='utf-8') as fr:
            L = fr.readlines()
            L.reverse()
            print(L)
            flag = False
            count = len(L)
            for line in L:
                lines = line.split('0A')
                print(lines[0].strip(), lines[1].strip(), lines[2].strip(), lines[3].strip(), lines[4].strip().split('/')[-1])
                if -1 == self.search_commitExist(lines[0].strip()):
                    if flag:
                        self.add(lines[0].strip(), lines[1].strip(), lines[2].strip(), lines[3].strip(), lines[4].strip().split('/')[-1])
                    else:
                        print('database not complete')
                        self.commit()
                        self.close()
                        return False
                else:
                    flag = True
                    print('commit exits', lines[0].strip())

            self.commit()
            self.close()


if __name__ == '__main__':
    db = Gitlog('database.db')


    if not db.gendatebase():
        os.system('cd /home/zhengsen/jenkins/workspace/gerrit_commit; git log --all --pretty=format:"%H 0A %an 0A %aI 0A %s 0A %S"  > /home/zhengsen/release_version/gitlog.txt')
        db.gendatebase()

    # ret = db.search_commitToId('be0f67f64f37a3bde2617e495208516249ccbb13')
    # print(ret)

    # ret = db.search_idToCommit(3206)
    # print(ret)

    print('Hello world')
