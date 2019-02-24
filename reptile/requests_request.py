import requests

hd = {'user-agent':'Chrome/56'};

params=None; #参数
data=None; #数据
headers=None; #html头
cookies=None;  #cookie
files=None;  #文件
auth=None; #认证
timeout=None;  #超时
allow_redirects=True; #重定向开关
proxies=None;  #代理
hooks=None;  
stream=None;  #立即下载
verify=None;  #认证ssl证书开关
cert=None; #本地SSL证书开关
json=None;  #json格式

requests.get()
requests.head()
requests.POST()
requests.put()
requests.patch()
requests.delete()

r = requests.request('POST', 'http://www.baidu.com', headers=hd)
print(r.headers)