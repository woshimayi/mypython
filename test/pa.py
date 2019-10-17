import os
import urllib
import re

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	print '1231231231231'
	return html

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x += 1
	print '222222222'
	return imglist

html = getHtml("http://cn.bing.com/images/search?q=%E8%8B%B1%E5%9B%BD%E8%AE%AE%E4%BC%9A%E5%A4%A7%E5%8E%A6%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB&FORM=ISTRTH&id=F1E1C03F7EB1F290F78351F68318CB06438FD2B9&cat=%E4%BB%8A%E6%97%A5%E7%83%AD%E5%9B%BE&lpversion=")
print  getImg(html)



# s= os.path.abspath('.')
# s = os.path.join(s, '456.txt')

# with open(s,'w') as f:
# 	print >> f , img