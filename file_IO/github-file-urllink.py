# -*- coding: UTF-8 -*-

# <!DOCTYPE html>
# <html lang="en">
# <head>
# 	<meta charset="UTF-8">
# 	<title>链接</title>
# </head>
# <body>
# 	<a href="http://www.baidu.com" target="_blank">百度网</a>
# </body>
# </html>
import linecache
import os
import sys


html = """
<!DOCTYPE html>
<html lang="en">
<head>
<style>
	#header {
	    background-color:black;
	    color:white;
	    text-align:center;
	    padding:5px;
	}
	#nav {
	    line-height:30px;
	    background-color:#eeeeee;
	    # height:1000px;
	    width:200px;
	    float:left;
	    padding:5px;
	}
	#section {
	    width:350px;
	    float:left;
	    padding:10px;
	}
	#footer {
	    background-color:black;
	    color:white;
	    clear:both;
	    text-align:center;
	   padding:5px;
	}
</style>
	<meta charset="UTF-8">
	<title>链接</title>
</head>
<body>
	<div id="header">
		<h1>mypython</h1>
	</div>
	<div id="nav">
		London<br>
		Paris<br>
		Tokyo<br>
	</div>
<section>
"""

htmlTail = """
			</section>
			<div id="footer">
				<a href="https://github.com/woshimayi/mypython" target="_blank">mypython</a></p>
			</div>
			</body>
			</html>
"""


dir  = r'/home/zs/Doc/mypython/GUI'
githubPrefix = r'https://github.com/woshimayi/mypython/'

def function(dir, file):
	print("==========os.walk================")
	index = 1  
	with open('./456.html', 'w') as f:
		f.write(html)

		for root,dirs,files in os.walk(dir):
			print("root=%s, dirs=%s, files=%s" % (root, dirs, files))
			githubDir = githubPrefix + root
			if ".git" not in githubDir:
				f.write("	<p><h3><a href=\""+githubDir+"blob/master/"+ "\" target=\"_blank\">"+root+"</a></h3></p>")

			for filepath in files:
				if os.path.splitext(filepath)[1] in file:
					githuburl = githubPrefix + root + "/"+ filepath
					# 添加文件功能描述
					# getline_desc = root + "/" + filepath
					# desc = linecache.getline(getline_desc, 10).strip()
					# print('github link url', githuburl)

					# print("============", filepath)
					# try:
					# 	if 'desc' in desc:
					# 		print('desc', desc, filepath)
					# 		url = desc.split(':')[-1]
					# 		f.write(u"		<p><a href=\"" + githuburl + "\" target=\"_blank\">" + filepath + ": " + url +"</a></p>\n")
					# 	else:
					# 		f.write(u"		<p><a href=\"" + githuburl + "\" target=\"_blank\">" + filepath + "</a></p>\n")
					# except:
					# 	pass
					# os.startfile(exec)  # 执行文件
					f.write(u"		<p><a href=\"" + githuburl + "\" target=\"_blank\">" + filepath + "</a></p>\n")
			# for sub in dirs:
			# 	print('dir', os.path.join(root,sub))
		f.write(htmlTail)


if __name__=="__main__":
	# file = input("Enter your input: ")
	# print(file)
	print(len(sys.argv))
	if len(sys.argv) < 2:
		print("fail get error < 2")
		sys.exit()
	dir = sys.argv[1]
	print(dir)
	function(dir, [".py"])
	print("finsh")
