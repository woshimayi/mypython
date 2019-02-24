from bs4 import BeautifulSoup
import requests
import re
import os
import time
import xlwt
import xlrd
import xlutils.copy

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
		f = open(name, 'wb')
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
			# if 'http'  in jpg_url['src']:k
			print(jpg_url['alt'],"	", jpg_url['src'],"		", str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
				# self.save_img(jpg_url['src'], jpg_url['alt']+'.jpg')
			print('成功')


# 获取首页中的连接地址
	def get_next_url(self, url):
		base_url = 'https://cn.bing.com/'
		r = requests.get(url, headers=self.headers)
		r.encoding='utf-8'
		soup=BeautifulSoup(r.text,"lxml")
		soup.prettify()
		jpg_next_url = ''
		i = 0

		workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
		sheet = workbook.add_sheet('url_0', cell_overwrite_ok=True)

		for jpg_url in soup.find_all('a'):
			if '美女' in jpg_url['href']:
				i += 1
				if 'http' in jpg_url['href']:
					jpg_next_url = jpg_url['href']
				else:
					jpg_next_url = base_url+jpg_url['href']
				print(jpg_next_url)
				sheet.write(i,0, jpg_next_url)
			workbook.save(r'./bing_pic.xls')

		data   = xlrd.open_workbook(r'./bing_pic.xls')
		table1 = data.sheets()[0]
		nrows = table1.nrows
		print(nrows)

		j = 0
		for pic_url_2 in range(nrows):
			j += 1
			sheet1 = workbook.add_sheet('url_'+str(j), cell_overwrite_ok=True)
			workbook.save(r'./bing_pic.xls')
			jpg_next_url = table1.cell_value(j,0)

			if jpg_next_url:
				r1 = requests.get(jpg_next_url, headers=self.headers)
				r1.encoding='utf-8'
				soup1=BeautifulSoup(r1.text,"lxml")
				soup1.prettify()

				k = 0
				for jpg_next_next_url in soup1.find_all('a'):
					if 'imagesize-large' in jpg_next_next_url['href']:
						jpg_next_next_next_url = base_url+jpg_next_next_url['href']
						print('成功')
						sheet1.write(0, 0, jpg_next_next_next_url)
						# print(jpg_next_next_next_url)
						break
				workbook.save(r'./bing_pic.xls')


			# 	if jpg_next_next_next_url:
			# 		r2 = requests.get(jpg_next_next_next_url, headers=self.headers)
			# 		r2.encoding='utf-8'
			# 		soup2=BeautifulSoup(r2.text,"lxml")
			# 		soup2.prettify()

			# 		for jpg_url_1 in soup2.find_all('a'):
			# 			time.sleep(0.2)
			# 			if 'http' in jpg_url_1['href'] and 'image' in jpg_url_1['href']:
			# 				jpg_url_2 = base_url+jpg_url_1['href']
			# 				print(jpg_url_2)

			# 				r3 = requests.get(jpg_url_2, headers=self.headers)
			# 				r3.encoding='utf-8'
			# 				soup3=BeautifulSoup(r3.text,"lxml")
			# 				soup3.prettify()

			# 				for jpg_url_3 in soup3.find_all('img'):
			# 					if 'http' in jpg_url_3['src']:
			# 						print(jpg_url_3['src'])
			# 						self.save_img(jpg_url_3['src'], str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
			# 						break





if __name__ == '__main__':
	be = BeautifulPicture()
	path = r'E:/get_big_pic'
	url = 'https://cn.bing.com/images/trending?form=Z9LH'
	be.mk_dir(path)
	be.get_next_url(url)





