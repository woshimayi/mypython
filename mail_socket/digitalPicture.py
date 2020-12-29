from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys

base_url = 'https://www.dgtle.com/'
url = 'https://www.dgtle.com/article-1574425-1.html'

class BeautifulPicture:
	def __init__(self):
		self.headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
		'authorization': ""
		}

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

	def save_img(self, url, name):
		img = requests.get(url)
		print('1')
		f = open(name, 'wb')
		print('2')
		f.write(img.content)
		print(name, '保存成功')
		f.close()



	def get_pic(self, url):
		r = requests.get(url, headers=self.headers)
		r.encoding='utf-8'
		soup=BeautifulSoup(r.text,"lxml")
		soup.prettify()
		i = 0
		for jpg_url in soup.find_all('img'):
			i += 1
			# print(jpg_url['src'])
			time.sleep(0.5)
			if 'http'  in jpg_url['src']:
				# print(jpg_url['alt'])
				print(str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
				self.save_img(jpg_url['src'], str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
				# print('成功')

	def get_next_url(self):

		for jpg_url in soup.find_all('a'):
			if 'http' in jpg_url['href']:
				print(jpg_url['href'])
				# print('成功')
			else:
				print(base_url+jpg_url['href'])

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("argc less three")
	be = BeautifulPicture()
	path = r'./get_pic'+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
	be.mk_dir(path)
	print(sys.argv)
	be.get_pic(sys.argv[1])
