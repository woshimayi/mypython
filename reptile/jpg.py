from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import re


headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
		'authorization': ""
		}

url = 'https://cn.bing.com/images/trending?form=Z9LH'
r = requests.get(url, headers=headers)
# print(r.text)
r.encoding='utf-8'

#下面代码示例都是用此文档测试
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# markup="<b><!--Hey, buddy. Want to buy a used parser?--></b>"


soup=BeautifulSoup(r.text,"lxml")
soup.prettify()


def mk_dir(path):
		path = path.strip()
		is_exit = os.path.exists(path)
		if not is_exit:
			print("创建", path, '文件夹')
			os.makedirs(path)
			print('创建成功')
		else:
			print(path, '文件夹已经存在')
		os.chdir(path)


# def get_next_url():
# 获取首页中的连接地址
base_url = 'https://cn.bing.com/'
for jpg_url in soup.find_all('a'):
	if '美女' in jpg_url['href']:
		if 'http' in jpg_url['href']:
			print(jpg_url['href'])
			# print('成功')
		else:
			print(base_url+jpg_url['href'])


# 进行连接地址post请求参数组合
for jpg_url in soup.find_all('img'):
	i += 1
	if 'http'  in jpg_url['src']:
		print(jpg_url['alt'])
		# print(jpg_url['alt'],"	", jpg_url['src'],"		", str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
		# self.save_img(jpg_url['src'], str(time.strftime("%Y%m%d%H%M%S", time.localtime()))+str(i)+'.jpg')
	# print('成功')







# print(soup.name)
# print(soup.head.link['href'])
# print(soup.head.contents)
# print(soup.head.contents.contents)
# print(soup.head.contents[2])
# for child in soup.head.children:
# 	print(child)
# print(soup.head.contents[2]['href'])
# for child in soup.head.descendants:
# 	print(child)
# print(len(list(soup.head.children)))
# print(len(list(soup.head.descendants)))

# print(soup.title.contents)
# print(soup.title.string)

# for string in soup.head.strings:
# 	print(repr(string))

# for string in soup.head.stripped_strings:
# 	print(repr(string))

# print(soup.title.string)
# print(soup.title.string.parent)

# print(soup.html)
# print(soup.html.parent.name)



# for parent in soup.div.parents:
# 	if parent is None:
# 		print(parent)
# 	else:
# 		print(parent.name)


# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='hp_cellCenter'))
# print(soup.div)
# print(soup.div.prettify())
# print(soup.a.next_sibling)
# print(soup.find_all('div'))

# for sibling in soup.a.next_siblings:
# 	print(repr(sibling))

# for sibling in soup.find(id='bgLink').next_siblings:
# 	print(repr(sibling))
# print(soup.find(id='bgLink'))
# print(soup.find(id='bgLink').next_element)
# for link in soup.find_all(True):
# 	print(link.get('href'))
# 	
# print(soup.find_all('a'))

# for tag in soup.find_all(re.compile("t")):
# 	print(tag.name)

# print(soup.find_all(['a', 'b']))

# for tag in soup.find_all(True):
# 	print(tag.name)



# def has_class_no_id(tag):
# 	return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_no_id))

# def not_lacie(href):
# 	return href
# print(soup.find_all(href=True).get('href'))


# def surrounded_by_strings(tag):
# 	return (isinstance(tag.next_element, NavigableString)) and isinstance(tag.previous_element, NavigableString)
# for tag in soup.find_all(surrounded_by_strings):
# 	print(tag.name)

# print(soup.find_all('head'))
# print(soup.find_all(id="officemenu_onenote"))
# print(soup.find_all(href=re.compile("notebook")))
# print(soup.find_all(id=True))

# print(soup.find_all(id='bgLink', href=re.compile("hprichbg")))

# print(soup.find_all(attrs={'class': 'sh_hide'}))

# print(soup.find_all('img', class_="sh_hide"))

# print(soup.select("html head title"))
print()
print()
print()


# img = requests.get('/sa/simg/SharedSpriteDesktopRewards_022118.png')
# f = open('123.jpg', 'wb')
# f.write(img.content)
# print('123', '保存成功')
# f.close()

# soup=BeautifulSoup(html_doc,"lxml")
# print(soup.a)
# print(soup.a.string)
# print(soup.head.string)
# print(soup.html)
# print(soup)   #BeautifulSoup对象为文档的全部内容

# soup1=BeautifulSoup(markup,"lxml")
# comment=soup1.b.string
# print(soup)   #BeautifulSoup对象为文档的全部内容
# print(tag)   #Tag标签对象
# print(comment)   #Comment对象包含文档注释内容
# print(navstr)    #NavigableString对象包装字符串内容