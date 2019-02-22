from bs4 import BeautifulSoup
import requests
import re
import os




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

		for jpg_url in soup.find_all('img'):
			# if 'http'  in jpg_url['src']:
			print(jpg_url['alt'],"	", jpg_url['src'],"		", jpg_url['alt']+'.jpg')
				# self.save_img(jpg_url['src'], jpg_url['alt']+'.jpg')
			print('成功')





if __name__ == '__main__':
	be = BeautifulPicture()
	path = r'E:/get_pic'
	url = 'https://cn.bing.com/images/trending?form=Z9LH'
	url1 = 'https://cn.bing.com/images/search?q=%E6%B8%85%E7%BA%AF%E5%B0%91%E5%A5%B3&FORM=ISTRTH&id=5A5E98350E94113A95927E7180669702492AFEB5&cat=%E7%BE%8E%E5%A5%B3&lpversion='
	be.mk_dir(path)
	be.get_pic(url1)





