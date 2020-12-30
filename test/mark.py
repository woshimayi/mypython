from bs4 import BeautifulSoup
import requests
import bs4
import tushare as ts
 
 
#获取源码
def check_link(url):
    try:
         
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！')
 
 
#解析并抓取
'''<br>print 部分，获取了9条信息，改变这部分参数，可以获取一共21条信息。<br>'''
def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')
    
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)
    print(ulist[1][3],ulist[3][3],ulist[5][3],ulist[7][3],ulist[8][3],ulist[13][3],ulist[15][3],ulist[16][3],ulist[17][3])
 
         
     
#定义主函数
def main():
    df = ts.get_stock_basics()
 
    for i in df.index:
        index_int = int(i)
        urli = []
        url = "http://www.cninfo.com.cn/information/brief/shmb%d.html"+index_int
        try:
            rs = check_link(url)
            get_contents(urli,rs)
            continue
        except:
            pass
                
         
main()