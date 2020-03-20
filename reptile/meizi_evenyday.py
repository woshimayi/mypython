from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys
from collections import OrderedDict

base_url = 'https://www.dgtle.com/'
url = 'https://www.dgtle.com/article-1574425-1.html'

class BeautifulPicture:
	def __init__(self):
		self.headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
					'Referer': 'https://www.mzitu.com/all'}
		self.headers2 = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
			'Referer': 'https://www.mzitu.com/all'}
		self.headers3 = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			'Referer': 'https://www.mzitu.com/all'}


	def mk_dir(self, path):
		self.path = path.strip()
		self.is_exit = os.path.exists(path)
		if not self.is_exit:
			print("创建", path, '文件夹')
			os.makedirs(path)
			print('创建成功')
		else:
			print(path, '文件夹已经存在')
		os.chdir(path)


	# 得到http://www.mzitu.com/all这个网址所有的相册的链接
	# site为站点网址，默认为http://www.mzitu.com/all
	def Get_Page_All_Url(self, siteUrl, num):
		# 设置代理IP访问
		# 抓捕解析网站过程中的错误
		try:
			req = requests.get(siteUrl, headers=self.headers2 )
			req.encoding = 'utf-8'
			bsObj = BeautifulSoup(req.text, "lxml")
			bsObj.prettify()
		except UnicodeDecodeError as e:
			print("-----UnicodeDecodeError url", siteUrl)
		except urllib.error.URLError as e:
			print("-----urlError url:", siteUrl)
		except socket.timeout as e:
			print("-----socket timout:", siteUrl)
		i = 0
		photoAlbumDic = OrderedDict()  # 声明字典,并排序
		print("正在连接到网站" + siteUrl)
		# 正则匹配相册链接标签
		for templist in bsObj.findAll("a", href=re.compile("https://www.mzitu.com/([0-9]+)")):
			i = i + 1
			photoAlbumUrl = templist.attrs['href']
			if num == 1:
				photoAlbumName = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + "-" + templist.get_text()
			else:
				photoAlbumName = str(i) + "-" + templist.get_text()
			# print(str(i) + "  " + photoAlbumName + " " + photoAlbumUrl)
			# photoAlbumUrl=str(i)+"  "+photoAlbumName+" "+photoAlbumUrl
			photoAlbumDic[photoAlbumName] = photoAlbumUrl
			if num == i:
				break

		# photoAlbumDicNew=OrderedDict(photoAlbumDic)

		return photoAlbumDic  # 返回相册名称：相册链接字典


	# 获取当前相册内所有的图片页面链接
	# photoAlbumurl为相册链接
	def Get_Photo_Album_Page_Url(self, photoAlbumurl):
		# 设置代理IP访问
		try:
			# time.sleep(1)
			# req = request.Request(photoAlbumurl, headers=headers1 or headers2 or headers3)
			req = requests.get(photoAlbumurl, headers=self.headers2 )
			req.encoding = 'utf-8'
			bsObj = BeautifulSoup(req.text, "lxml")
			bsObj.prettify()
		except UnicodeDecodeError as e:
			print("-----UnicodeDecodeError url", photoAlbumurl)

		bianhaolist = []  # 声明页面编号list,为的是找出这个页面中最大的页面编号
		photoAlbumPageUrlList = []  # 存储该网页下所有的相册链接
		print("正在连接到" + photoAlbumurl + ",并解析该链接的页面链接")
		if bsObj != "":
			for pagelist in bsObj.findAll("div", {"class": "pagenavi"}):
				# 正则匹配相册链接
				for link in pagelist.findAll("a", href=re.compile("https://www.mzitu.com/([0-9]+)/([0-9]+)*$")):
					lianjie = link.attrs['href']
					# print(link.attrs['href'])
					bianhao = lianjie.replace(photoAlbumurl + "/", "")  # 得到编号
					# print(bianhao)
					bianhaolist.append(int(bianhao))  # 添加到编号列表
			bianhaoMax = max(bianhaolist)  # 找到图片链接最大编号
			for i in range(1, bianhaoMax + 1):
				photoAlbumPageUrl = photoAlbumurl + "/" + str(i)  # 得到每个相册的图片的链接
				# print(photoAlbumPageUrl)
				photoAlbumPageUrlList.append(photoAlbumPageUrl)
		return photoAlbumPageUrlList  # 返回图片链接列表


	def get_pic(self, url):
		r = requests.get(url, headers=self.headers1)
		r.encoding='utf-8'
		soup=BeautifulSoup(r.text,"lxml")
		soup.prettify()
		i = 0
		for jpg_url in soup.findAll("div", {"class": "main-image"}):
			for imgUrl in jpg_url.findAll('img'):
				print(imgUrl['src'])
				i += 1
				time.sleep(8)
				self.save_img(imgUrl['src'], str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')


	def get_next_url(self):
		for jpg_url in soup.find_all('a'):
			if 'http' in jpg_url['href']:
				print(jpg_url['href'])
				# print('成功')
			else:
				print(base_url+jpg_url['href'])
		# print('成功')


	def save_img(self, url, name):
		img = requests.get(url)
		f = open(name, 'wb')
		f.write(img.content)
		print(url, name, '保存成功')
		f.close()


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("argc less three")
	i = 0
	be = BeautifulPicture()
	photoAlbum = be.Get_Page_All_Url("http://www.mzitu.com/all", 1)

	for photoAlbumurllist in photoAlbum.keys():
		print("相册名字 " + photoAlbumurllist)  # 相册名字
		print(photoAlbum[photoAlbumurllist])
		be.mk_dir(photoAlbumurllist)
		photoAlbumurllists = be.Get_Photo_Album_Page_Url(photoAlbum[photoAlbumurllist])
		for picture_Url in photoAlbumurllists:
			i = i+1
			# print(picture_Url)
			time.sleep(0.5)
			be.get_pic(picture_Url)


	# be.get_pic(sys.argv[1])
