
import  re

# pattern = re.compile(r'hello')

# match = pattern.match('hello world')

# if match:
# 	print match.group()

sen = 'http://tse4.mm.bing.net/th?id=OIP.Eth0zoGt0-nDU-t6BIL7SQEsDI&amp;w=230&amp;h=170&amp;rs=1&amp;pcl=dddddd&amp;pid=1.1" alt=" "/></div></a><div class="meta"><a class="tit" target="_blank" href="http://news.dahe.cn/2016/02-09/106429285.html" h="ID=images,5014.1">news.dahe.cn</a><div class="des">... \xe6\x81\x90\xe6\x80\x96\xe8\xa2\xad\xe5\x87\xbb(\xe5\x9b\xbe)_\xe6\x96\xb0\xe9\x97\xbb\xe4\xb8\xad\xe5\xbf\x83_\xe5\xa4\xa7\xe6\xb2\xb3\xe7\xbd\x91</div><div class="fileInfo">300 x 200 jpeg 12kB</div></div></div><div class="item"><a class="thumb" target="_blank" href="http://gb.cri.cn/mmsource/images/2010/11/23/ny101123001.jpg', 'http://tse3.mm.bing.net/th?id=OIP.m6sRBdc5txZL2WNnnLFCBAEsC8&amp;w=230&amp;h=170&amp;rs=1&amp;pcl=dddddd&amp;pid=1.1" alt=" "/></div></a><div class="meta"><a class="tit" target="_blank" href="http://'

with open('./333.txt', 'w') as f:
	
	while 1:
	    
	    mm = re.search("\d,\d", sen)
	    
	    if mm:
	        mm = mm.group()
	        sen = sen.replace(mm, mm.replace(",", "\n"))
	        print sen
	    else:
	        break


