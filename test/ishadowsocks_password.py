#net.py
#@author imkh 
#modify by qixuxiang
import urllib.request
import urllib.parse
import re
import subprocess
import json
url = "http://www.ishadowsocks.net/"
res = urllib.request.urlopen(url)
content = res.read()
content=content.decode('utf-8')#转化为utf-8
#pattern = re.compile('<div.*?col-sm-4 text-center">.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>.*?<font.*>.*?</h4>.*?<h4>(.*?)</h4>.*?</div>',re.S)
pattern = re.compile('<div.*?col-sm-4 text-center">.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>',re.S)
items = re.findall(pattern,content)
password1 = items[0][2].split(":")[1]#USA

password2 = items[1][2].split(":")[1]#HK
password3 = items[2][2].split(":")[1]#JP

'''
print(content)
print(password1)
print(password2)
print(password3)
'''
subprocess.call('taskkill /f /im shadowsocks.exe',stdout=subprocess.PIPE)
#更换为你的ss配置文件路径
ssconfigpath = "D:\Shadowsocks-2.5.8\gui-config.json"
with open(ssconfigpath,"r+") as f:
    data = json.load(f)
    data[u"configs"][0][u"password"] = password3
    f.seek(0)
    json.dump(data,f,indent=4)

#更改为你的ss程序路径
sspath = "D:\Shadowsocks-2.5.8\Shadowsocks.exe"
subprocess.Popen(sspath)
print("ok!")