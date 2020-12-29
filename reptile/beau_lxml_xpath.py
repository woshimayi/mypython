# desc: beautiful lxml xpath re python库性能对比


import re
import sys
import time
import requests
from lxml.html import fromstring
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as bs

def Timer():
    a = time.time()
    while True:
        c = time.time()
        yield time.time()-a
        a = c
timer = Timer()
url = "http://www.python.org/"
html = requests.get(url).text
num = 10000
print ('\n==== Python version: %s =====' %sys.version)
print ('\n==== Total trials: %s =====' %num)
next(timer)
soup = bs(html, 'lxml')
for x in range(num):
    paragraphs = soup.findAll('p')
t = next(timer)
print ('bs4 total time: %.1f' %t)

d = pq(html)
for x in range(num):
    paragraphs = d('p')
t = next(timer)
print ('pq total time: %.1f' %t)

tree = fromstring(html)
for x in range(num):
    paragraphs = tree.cssselect('p')
t = next(timer)
print ('lxml (cssselect) total time: %.1f' %t)

tree = fromstring(html)
for x in range(num):
    paragraphs = tree.xpath('.//p')
t = next(timer)
print ('lxml (xpath) total time: %.1f' %t)

for x in range(num):
    paragraphs = re.findall('<[p ]>.*?</p>', html)
t = next(timer)
print ('regex total time: %.1f (doesn\'t find all p)\n' %t)