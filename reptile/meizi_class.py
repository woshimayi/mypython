
# 得到妹子图网站所有图片，输入网址为http://www.mzitu.com/all
# __author__ = 'Administrat
# coding=utf-8

import io
import os
import sys
import math
import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import time
import socket
from collections import OrderedDict

socket.setdefaulttimeout(5000)  # 设置全局超时函数

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8'

# 设置不同的headers,伪装为不同的浏览器
headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
            'Referer': 'https://www.mzitu.com/all'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36', 'Referer': 'https://www.mzitu.com/all'}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Referer': 'https://www.mzitu.com/all'}


# 在指定路径创建文件夹
def CreateDirectory(DirectoryName):
    DirectoryNameNew = []  # 创建新的存储列表
    if DirectoryName == "":  # 如果传进来的文件夹名为空
        DirectoryNameNew = "新建文件夹"
    for l in DirectoryName:  # 如果文件夹名不为空，剔除其中的“/”
        if l != "/" and l != "\\":
            DirectoryNameNew.append(l)




    root = r".\妹子图"
    path = root + "".join(DirectoryNameNew)  # join将列表转为为字符串
    print("创建相册" + root + "".join(DirectoryNameNew))
    try:
        os.makedirs(path)
    except Exception as e:
        print(root + "".join(DirectoryNameNew) + "已经存在")

    return path


# 得到http://www.mzitu.com/all这个网址所有的相册的链接
# site为站点网址，默认为http://www.mzitu.com/all
def GetXiangceUrl(siteUrl):
    # 设置代理IP访问
    # 抓捕解析网站过程中的错误
    try:
        # time.sleep(1)
        #req = request.Request(siteUrl, headers=headers1 or headers2 or headers3)
        req = request.Request(siteUrl, headers=headers1)
        html = urlopen(req)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        html.close()
    except UnicodeDecodeError as e:
        print("-----UnicodeDecodeError url", siteUrl)
    except urllib.error.URLError as e:
        print("-----urlError url:", siteUrl)
    except socket.timeout as e:
        print("-----socket timout:", siteUrl)
    i = 0
    XiangceZidian = OrderedDict()  # 声明字典,并排序
    print("正在连接到网站" + siteUrl)
    # 正则匹配相册链接标签
    for templist in bsObj.findAll("a", href=re.compile("https://www.mzitu.com/([0-9]+)")):
        i = i + 1
        xiangceUrl = templist.attrs['href']
        xiangceName = str(i) + "   " + templist.get_text()
        print(str(i)+"  "+xiangceName+" "+xiangceUrl)
        # XiangceUrl=str(i)+"  "+xiangceName+" "+xiangceUrl
        XiangceZidian[xiangceName] = xiangceUrl
        # XiangceZidianNew=OrderedDict(XiangceZidian)

    return XiangceZidian  # 返回相册名称：相册链接字典


# 获取当前相册内所有的图片页面链接
# xiangceurl为相册链接
def GetXiangcePageUrl(xiangceurl):
    # 设置代理IP访问
    try:
        # time.sleep(1)
        #req = request.Request(xiangceurl, headers=headers1 or headers2 or headers3)
        req = request.Request(xiangceurl, headers=headers1)
        html = urlopen(req)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        html.close()
    except UnicodeDecodeError as e:
        print("-----UnicodeDecodeError url", xiangceurl)
    except urllib.error.URLError as e:
        print("-----urlError url:", xiangceurl)
    except socket.timeout as e:
        print("-----socket timout:", xiangceurl)

    bianhaolist = []  # 声明页面编号list,为的是找出这个页面中最大的页面编号
    XiangCePageUrlList = []  # 存储该网页下所有的相册链接
    print("正在连接到" + xiangceurl + ",并解析该链接的页面链接")
    if bsObj != "":
        for pagelist in bsObj.findAll("div", {"class": "pagenavi"}):
            # 正则匹配相册链接
            for link in pagelist.findAll("a", href=re.compile("https://www.mzitu.com/([0-9]+)/([0-9]+)*$")):
                lianjie = link.attrs['href']
                # print(link.attrs['href'])
                bianhao = lianjie.replace(xiangceurl + "/", "")  # 得到编号
                # print(bianhao)
                bianhaolist.append(int(bianhao))  # 添加到编号列表
        bianhaoMax = max(bianhaolist)  # 找到图片链接最大编号
        for i in range(1, bianhaoMax + 1):
            XiangCePageUrl = xiangceurl + "/" + str(i)  # 得到每个相册的图片的链接
            # print(XiangCePageUrl)
            XiangCePageUrlList.append(XiangCePageUrl)
    return XiangCePageUrlList  # 返回图片链接列表


# 得到当前页面的图片链接
# XiangCePageUrl为当前相册某个页面的链接，path为文件夹路径，replaceurl为相册的链接
def GetPageImageUrl(XiangCePageUrl, path, replaceurl):
    # 设置代理IP访问
    try:
        # time.sleep(1)
        #req = request.Request(XiangCePageUrl, headers=headers1 or headers2 or headers3)
        req = request.Request(XiangCePageUrl, headers=headers1)
        html = urlopen(req)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        html.close()

        bianhao = XiangCePageUrl.replace(
            replaceurl + "/", "")  # 这里的编号每个相册图片的编号，例如XXXX1.jpg
        print("path:" + path)
        # 寻找图片链接以及名称

        for templist in bsObj.findAll("div", {"class": "main-image"}):
            for ImageUrllist in templist.findAll("img"):
                # print(ImageUrllist.attrs['src'])
                Imageurl = ImageUrllist.attrs['src']  # 图片链接
                print(XiangCePageUrl + "的图片链接为" + Imageurl)
                # print(ImageUrllist.attrs['alt'])
                ImageName = ImageUrllist.attrs['alt']  # 图片名称
                ImageNameNew = []  # 新的图片名称列表，为了剔除原有名称中包含的"/"符号
                for l in ImageName:
                    if l != "/" and l != " " and l != "\\" and l != ".":
                        ImageNameNew.append(l)
                if len(ImageNameNew) != 0:
                    print("正在下载文件：" + str(path) + "\\" + "".join(ImageNameNew) +
                          str(bianhao) + ".jpg")  # join将列表转为字符串
                    try:
                        ImageNameNewStr = ''.join(ImageNameNew)
                        localImagefilePath = os.path.join(
                            path, f"{ImageNameNewStr}{bianhao}.jpg")

                        # 第一种下载反盗链图片的方法
                        imageHeader = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0', 'Referer': XiangCePageUrl}
                        imagedata = requests.get(
                            Imageurl, headers=imageHeader).content
                        with open(localImagefilePath, 'wb') as f:
                            f.write(imagedata)

                        # 第二种下载反盗链图片的方法
                        # opener = urllib.request.build_opener()
                        # opener.addheaders = [('User-Agent',
                        #                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'),('Referer',XiangCePageUrl)]
                        # urllib.request.install_opener(opener)
                        # urllib.request.urlretrieve(Imageurl, localImagefilePath)

                        print("myper=" + str(myper))
                        while (True == jindu):  # 判断是否下载完成
                            print("下载完成！")
                            print('')
                            # time.sleep(1)#下载完成后sleep3秒，防止反爬虫机制
                            break
                    # else:
                    # time.sleep(10)#如果失败，先休眠10秒
                    # urlretrieve(Imageurl,str(path)+"\\"+"".jion(ImageNameNew)+str(bianhao)+".jpg",jindu)#再下载，直到下载完成
                    # time.sleep(3)
                    except Exception as e:
                        time.sleep(10)  # 如果失败，先休眠10秒
                        # urlretrieve(Imageurl,str(path)+"\\"+"".jion(ImageNameNew)+str(bianhao)+".jpg",jindu)#再下载，直到下载完成
                        # print("下载链接"+Imageurl+"出错,重新下载")
                        # time.sleep(3)

    except UnicodeDecodeError as e:
        print("-----UnicodeDecodeError url", XiangCePageUrl)
    except urllib.error.URLError as e:
        print("-----urlError url:", XiangCePageUrl)
    except socket.timeout as e:
        print("-----socket timout:", XiangCePageUrl)
    print("正在获取" + XiangCePageUrl + "的图片链接")


# urlretrieve()的回调函数，显示当前的下载进度
# a为已经下载的数据块
# b为数据块大小
# c为远程文件的大小
global myper


def jindu(a, b, c):
    if not a:
        print("连接打开")
    if c < 0:
        print("要下载的文件大小为0")
    else:
        global myper
        per = 100 * a * b / c

        if per > 100:
            per = 100
        myper = per
        print("myper0=" + str(myper))
        print("当前下载进度为：" + '%.2f%%' % per)
    if per == 100:
        return True


# GetXiangceUrl("http://www.mzitu.com/all")
# GetXiangcePageUrl("http://www.mzitu.com/85695")
# GetPageImageUrl("https://www.mzitu.com/85695/2","E:\Python\Python妹子图","https://www.mzitu.com/85695")
if __name__ == '__main__':
    XiangCe = GetXiangceUrl("http://www.mzitu.com/all")  # 返回字典,并将返回字典排序
    for xiangceurllist in XiangCe.keys():
        print("相册名字" + xiangceurllist)  # 相册名字
        # print(XiangCe.get(xiangceurllist))#相册链接
        mypath = CreateDirectory(xiangceurllist)
        # print(mypath)
        XiangCePageUrl = GetXiangcePageUrl(XiangCe.get(xiangceurllist))
        # time.sleep(1)
        # print(XiangCePageUrl)
        for xiangcepageurllist in XiangCePageUrl:
            # print(xiangcepageurllist)
            # print(XiangCePageUrl.index(xiangcepageurllist))
            GetPageImageUrl(xiangcepageurllist, mypath,
                            XiangCe.get(xiangceurllist))
            time.sleep(0.5)
