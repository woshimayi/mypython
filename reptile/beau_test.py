import requests
from bs4 import BeautifulSoup as bs

#获取单个页面的源代码网页
def gethtml(pagenum):
    url = 'http://www.qiushibaike.com/hot/page/'+str(pagenum)+'/?s=4949992'
    req = requests.get(url,headers = Headers)
    html = req.text
    #print(html)
    return html

#获取单个页面的所有段子
def getitems(pagenum):
    html = gethtml(pagenum)
    soup = bs(html,"html.parser")
    f = soup.find_all('div','content')
    items =[]
    for x in f:
        #print(x.get_text())
        items.append(x.get_text())
    #print(items)
    return items

#分别打印单个页面的所有段子        
def getduanzi(pagenum):
    n = 0
    for x in getitems(pagenum):
        n +=1
        print('第%d条段子：\n%s' % (n,x))

#分别打印所有页面的段子
def getall(bginpage,endpage):
   
    try:
        for pagenum in range(int(bginpage),int(endpage)+1):
            print(('----------华丽丽的分割线【第%d页】----------'% pagenum).center(66))
            getduanzi(pagenum)
    except:
        print('页码输入错误，只接收正整数输入。')   
    
if __name__ == '__main__':

    Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    bginpage = input('输入起始页：').strip()
    endpage = input('输入终止页：').strip()
    getall(bginpage,endpage)