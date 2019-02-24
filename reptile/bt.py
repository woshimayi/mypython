import requests
import re

# url = "http://www.btbtdy.tv/vidlist/12826.html"
# http://www.btbtdy.tv/down/12826-0-1.html

# for i in range():
# 	r = requests.get(url)
# 	print(r.text)
# 	
# 	

for page in range(1,20):
    url='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(page)+'.html'
    print(url)
    html=requests.get(url)
    html.encoding="gb2312"
    #print(html.text)
    data=re.findall('<a href="(.*?)" class="ulink">',html.text)  #返回的是列表
    #print(data)
    for m in data:
        xqurl = 'http://www.ygdy8.net'+m
        #print(xqurl)

        html2=requests.get(xqurl)
        html2.encoding='gb2312'#指定编码
        #print(html2.text)
        try:
            dyLink = re.findall('<a href="(.*?)">ftp://.*?</a></td>',html2.text)[0]
            print(dyLink)
        except:
            print("没有匹配信息")

        with open('movie.txt','a') as f:
            f.write(dyLink+'\n')
