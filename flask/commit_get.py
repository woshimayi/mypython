<<<<<<< HEAD
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: commit_get.py
@time: 23/7/13 15:22
@desc: 
'''
import socket

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    'authorization': ""
}


def get_commit(url):
    try:
        r = requests.get(url, headers=headers, timeout=2)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            print(r.text)
    except Exception as e:
        print(e)


def commit_sort():
    fw = open(r'commit.txt', 'w')
    with open(r'commit_tmp.txt', 'r') as f:
        a = f.readlines()
        for line in a[::-1]:
            fw.write(line)

    f.close()
    fw.close()

def commit_sort_1():
    fw = open(r'commit_tmp_1.txt', 'w', encoding='utf-8')
    with open(r'tar.txt', 'r', encoding='utf-8') as f:
        a = f.readlines()
        count = len(a)
        print(count)
        for line in a:
            count -= 1
            print(count, line.split(' ', 3))
            fw.write(line)

    f.close()
    fw.close()


def commit_html():
    gerrit_ip = '172.16.8.160'
    count = 0;
    fw = open(r'static/commit_html.html', 'w')

    fw.write('<?xml')
    fw.write('version="1.0" encoding="utf-8"?>')
    fw.write(
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
    fw.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">')
    fw.write('<head>')
    fw.write('<meta http-equiv="content-type" content="application/xhtml+xml; charset=utf-8"/>')
    fw.write('<link rel="stylesheet" type="text/css" href="static/gitweb-default.css"/>')
    fw.write('</head>')
    fw.write('<body>')
    fw.write('<table class="shortlog">')
    fw.write('<tr>')
    fw.write('<th>gitId</th>')
    fw.write('<th>commit</th>')
    fw.write('</tr>')

    with open(r'commit.txt', 'r') as fr:
        L = fr.readlines()
        L.reverse()
        print(L)
        count = len(L)
        for line in L:
            count -= 1
            print(line)
            if count % 2:
                fw.write('<tr class="dark">')
            else:
                fw.write('<tr class="light">')
            fw.write('<td class="Hg Id">')
            fw.write('	<a class="list" >{}</a>'.format(count))
            fw.write('</td>')

            fw.write('<td>')
            fw.write('	<a class="list subject" href="http://{}/gitweb?p=HSAN_091.git;a=commit;h={}">{}</a>'.format(
                gerrit_ip, line, line))
            fw.write('</td>')
            fw.write('</tr>')


    fw.write('</table>')
    # fw.write('<script type="text/javascript" src="js/gitweb.js"></script>')
    fw.write('<script src="{{ url_for(filename="js/gitweb.js.js") }}"></script>')
    fw.write('</body>')
    fw.write('</html>')


def IsOpen(ip, port):
    """
    检测端口是否打开
    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(1)
        return True
    except:
        return False


if __name__ == '__main__':
    # if IsOpen('172.16.8.160', '8056'):
    #     get_commit('http://172.16.8.160:8056/f6988763282ce9748f664765c7e9e021a162f795')
    # else:
    #     get_commit('http://172.16.8.160:8056/f6988763282ce9748f664765c7e9e021a162f795')

    # commit_html()
    commit_sort_1()

    print('Hello world')
    exit

# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: commit_get.py
@time: 23/7/13 15:22
@desc: 
'''
import socket

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    'authorization': ""
}


def get_commit(url):
    try:
        r = requests.get(url, headers=headers, timeout=2)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            print(r.text)
    except Exception as e:
        print(e)


def commit_sort():
    fw = open(r'commit.txt', 'w')
    with open(r'commit_tmp.txt', 'r') as f:
        a = f.readlines()
        for line in a[::-1]:
            fw.write(line)

    f.close()
    fw.close()

def commit_sort_1():
    fw = open(r'commit_tmp_1.txt', 'w', encoding='utf-8')
    with open(r'tar.txt', 'r', encoding='utf-8') as f:
        a = f.readlines()
        count = len(a)
        print(count)
        for line in a:
            count -= 1
            print(count, line.split(' ', 3))
            fw.write(line)

    f.close()
    fw.close()


def commit_html():
    gerrit_ip = '172.16.8.160'
    count = 0;
    fw = open(r'static/commit_html.html', 'w')

    fw.write('<?xml')
    fw.write('version="1.0" encoding="utf-8"?>')
    fw.write(
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
    fw.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">')
    fw.write('<head>')
    fw.write('<meta http-equiv="content-type" content="application/xhtml+xml; charset=utf-8"/>')
    fw.write('<link rel="stylesheet" type="text/css" href="static/gitweb-default.css"/>')
    fw.write('</head>')
    fw.write('<body>')
    fw.write('<table class="shortlog">')
    fw.write('<tr>')
    fw.write('<th>gitId</th>')
    fw.write('<th>commit</th>')
    fw.write('</tr>')

    with open(r'commit.txt', 'r') as fr:
        L = fr.readlines()
        L.reverse()
        print(L)
        count = len(L)
        for line in L:
            count -= 1
            print(line)
            if count % 2:
                fw.write('<tr class="dark">')
            else:
                fw.write('<tr class="light">')
            fw.write('<td class="Hg Id">')
            fw.write('	<a class="list" >{}</a>'.format(count))
            fw.write('</td>')

            fw.write('<td>')
            fw.write('	<a class="list subject" href="http://{}/gitweb?p=HSAN_091.git;a=commit;h={}">{}</a>'.format(
                gerrit_ip, line, line))
            fw.write('</td>')
            fw.write('</tr>')


    fw.write('</table>')
    # fw.write('<script type="text/javascript" src="js/gitweb.js"></script>')
    fw.write('<script src="{{ url_for(filename="js/gitweb.js.js") }}"></script>')
    fw.write('</body>')
    fw.write('</html>')


def IsOpen(ip, port):
    """
    检测端口是否打开
    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(1)
        return True
    except:
        return False


if __name__ == '__main__':
    # if IsOpen('172.16.8.160', '8056'):
    #     get_commit('http://172.16.8.160:8056/f6988763282ce9748f664765c7e9e021a162f795')
    # else:
    #     get_commit('http://172.16.8.160:8056/f6988763282ce9748f664765c7e9e021a162f795')

    # commit_html()
    commit_sort_1()

    print('Hello world')
    exit
