import urllib
import urllib2
import os

url = "http://www.baidu.com"
user_agent = ""
values = {"username":'asd',"password": "xxx"}

headers = {"user_Agent": user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)

page = response.read()


with open("./456.txt", 'w') as f:
	print >> f, page