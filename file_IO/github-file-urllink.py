# codeing=utf-8

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


dir  = r'/home/zs/Doc/mypython/'
githubPrefix = r'https://github.com/woshimayi/mypython/blob/master/'

def function(dir, file):
	print("==========os.walk================")
	index = 1  
	with open('./456.html', 'w') as f:
		f.write(html)

		for root,dirs,files in os.walk(dir):
			# print("root=%s, dirs=%s, files=%s" % (root, dirs, files))
			githubDir = githubPrefix + root.split('/', 5)[5]
			if ".git" not in githubDir:
				f.write("	<p><h3><a href=\""+githubDir+"\" target=\"_blank\">"+root.split('/', 5)[5]+"</a></h3></p>")
			if 5 <= len(root.split('/', 5)):
				for filepath in files:
					if os.path.splitext(filepath)[1] in file:
						githuburl = githubPrefix + root.split('/', 5)[5] + "/"+ filepath
						# print(githuburl)
						f.write("		<p><a href=\"" + githuburl + "\" target=\"_blank\">"+filepath+"</a></p>\n")
						# print('github link url', githuburl)
						# os.startfile(exec)  # 执行文件
			# for sub in dirs:
			# 	print('dir', os.path.join(root,sub))
		f.write(htmlTail)


if __name__=="__main__":
	# file = input("Enter your input: ")
	# print(file)
	# if len(sys.argv) == 3:
	function(dir, [".py"])
	print("finsh")
