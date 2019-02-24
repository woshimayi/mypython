import os
import requests 
import json
from requests import Request, Session

# from PIL import Image
# from io import BytesIO

# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# r = requests.post("http://www.baidu.com/post")
# print(r.status_code)

# payload = {'key1': 'value1', 'key2':'value2'}
# r = requests.get("http://www.baidu.com/post", params=payload)
# print(r.text)
# print(r.url)


# payload1 = {'key1': 'value1', 'key1':'value2'}
# r = requests.get("http://www.baidu.com/post", data=payload1)
# print(r.text)

# r = requests.get("http://www.btbtdy.tv/btdy/dy13303.html")
# print(r.text)


# r.content()
# i = Image.open(BytesIO(r.content))

# r = requests.get("http://www.baidu.com/timeline.json", stream=True)
# print(r.raw)
# print(r.raw.read(10))

# with open("./one.log", 'wb') as fd:
# 	for chunk in r.iter_content(chunk_size):
# 		fd.write(chunk)


# url = 'http://www.baidu.com'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r.encoding)
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.text)
# 

# payload = {'key1':'value1', 'key2':'value2'};
# r = requests.post("http://httpbin.org/post", data=payload);
# print(r.text)


# payload = (('key1', 'value1'), ('key1', 'value2'), ('key1', 'value3'));
# r = requests.post("http://httpbin.org/post", data=payload);
# 

# url = 'http://api.github.com/some/endpoint'
# payload = {'some':'data'}
# r = requests.post(url, data=json.dumps(payload))
# print(r.text)


# url = 'http://httpbin.org/post';
# files = {'file': open(report.xls, 'rb')};
# r = requests.post(url, files=files);
# print(r.text)


# url = 'http://httpbin.org/post'
# files = {'file': ('one.log', open('one.log', 'rb'), 'application/vnd.ms-excel', {'Expires':'0'})};
# r = requests.post(url, files=files)
# print(r.text)



# url = 'http://httpbin.org/post'
# files = {'file': ( 'some, data, to, send\r\nanother, row,to,send\r\n')};
# r = requests.post(url, files=files)
# print(r.text)

# r = requests.get('http://www.baidu.com');
# print(r.status_code)
# print(r.raise_for_status)

# print(r.headers['Content-Type']);
# print(r.headers.get('content-type'));

# print(r.status_code == requests.codes.ok)


# bad_r = requests.get('http://httpbin.org/status/404');
# print(bad_r.status_code);


# url = 'http://example.com/some/cookie/setting/url';
# r = requests.get(url);
# r.cookies['example_cookie_name']


# s = requests.Session()
# r = s.get('http://www.httpbin.com/cookies', cookies={'from-my':'browser'});
# print(r.text);


# s = requests.Session()
# s.auth = ('user', 'pass');
# s.headers.update({'x-test':'true'})

# r = s.get('http://www.httpbin.org/headers', headers={'x-test2': 'true'});
# print(r.text);



# url = 'http://www.baidu.com';
# s = Session()
# req = Request('GET', url,
# 	data='sdf',
# 	headers='hhhhhh'
# )
# prepped = req.prepare()

# resp = s.send(prepped, 
# 	stream=stream,
# 	verify=verify,
# 	proxies=proxies,
# 	cert=cert,
# 	timeout=timeout
# )

# print(resp.status_code)

# r = requests.get('https://ww.baidu.com', verify=True)
# r = requests.get('https://github.com', verify='/path/to/certfile')
# r = requests.get('https://www.baidu.com', verify=False);
# print(r)
# 

# url = 'http://httpbin.org';
# req = requests.request('GET', 'http://httpbin.org/get');
# print(req)

# requests.head(url, )
# 
# 

import time

# print(datetime.date.today().strptime('%Y%m%d%H%M%S'))
# print(datetime.datetime.now())
# print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S'))
print(time.strftime("%Y%m%d%H%M%S", time.localtime())) 