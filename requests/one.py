import os
import requests 
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


payload1 = {'key1': 'value1', 'key1':'value2'}
r = requests.get("http://www.baidu.com/post", data=payload1)
print(r.text)

# r = requests.get("http://www.baidu.com/timeline.json")
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