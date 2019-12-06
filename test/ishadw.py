# coding:utf-8
# 一键修改免费ss服务器密码配置
import requests
import re

#下载网页
def download(url):
    res = requests.get(url)
    return res.text

#设置相应的正则规则
re_div = re.compile(r"<div class=\"col-lg-4 text-center\">[\w\W]+?</div>")
re_server = re.compile(r"<h4>[\w\W]服务器地址:([\w\W]+?)</h4>")
re_port = re.compile(r"<h4>端口:(\d+)</h4>")
re_pwd = re.compile(r"<h4>[\w\W]密码:(\d+)</h4>")
re_method = re.compile(r"<h4>加密方式:([\w\W]+?)</h4>")

#过滤
def get0(n):
    if len(n):
        return n[0]
    else:
        return "";

if __name__=="__main__":
    url = "https://get.ishadowx.biz/"
    path = "gui-config.json"

    #下载网页
    html = download(url)
    html = re.findall(r"<section id=\"free\">[\w\W]+?</section>", html)[0]
    #获取数据并添加
    div = re_div.findall(html)
    for d in div:
        server = re_server.findall(d)
        port = re_port.findall(d)
        pwd = re_pwd.findall(d)
        method = re_method.findall(d)
        server = get0(server)
        port = get0(port)
        pwd = get0(pwd)
        method = get0(method)
        print("IP：\t\t"+server)
        print("端口：\t\t"+port)
        print("密码：\t\t"+pwd)
        print("------------------------")
    # input("按任意按键结束")