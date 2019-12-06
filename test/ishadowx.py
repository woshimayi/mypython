import sys,os
import requests
from bs4 import BeautifulSoup
import re
import json
import copy
import random




headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
		'authorization': ""
		}



html = requests.get("https://get.ishadowx.biz/", headers=headers)
# print(html.text)

soup=BeautifulSoup(html.text,"lxml")
# print(soup.prettify())


hrefs = soup.find_all('a', href=re.compile(".png"))

# print(hrefs)

for href in hrefs:
	print('https://get.ishadowx.biz/'+href.get('href'))

	img = requests.get('https://get.ishadowx.biz/'+href.get('href'))
	imgs = re.split(r'[/]' , href.get('href'))
	print(imgs[-1])

	f = open(imgs[-1], 'wb')
	f.write(img.content)
	print(imgs[-1], '保存成功')
	f.close()




