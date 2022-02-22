#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: ddns_dof.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/2/19 18:04
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/2/19 18:04
 * @Descripttion: 
'''

"""Powered By Jack---http://renjikai.com/
   Based On http://v2ex.com/t/200342 GPU"""

import urllib, time, json, hashlib, requests
from time import gmtime

"""Get Correct IP"""
params = urllib.urlencode({'ip': 'myip'})
f = urllib.urlopen("http://ip.taobao.com/service/getIpInfo2.php", params)
ddata = json.loads(f.read())
wan_ip = ddata['data']['ip']

"""Some Settings You Need To Set"""
api_url = "https://www.cloudxns.net/api2/record/238740"
api_key = "a7fe5ecbb823e7b0c968b2a885a18e98"
api_secret = "8575d2316d50406d"
Domain_ID = 11874
ttl = 120
line_id = 1
host = "home"
Domain_type = "A"

request_data = {
    "domain_id": Domain_ID,
    "host": host,
    "value": wan_ip,
    "type": Domain_type,
    "ttl": ttl,
    "line_id": line_id
}

request_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
hmac = hashlib.md5(api_key + api_url + str(json.dumps(request_data)) + request_time + api_secret).hexdigest()
headers = {
    'API-KEY': api_key,
    'API-REQUEST-DATE': request_time,
    'API-HMAC': hmac,
    'API-FORMAT': 'json'
}
""" ignore urlib3 warnings """

if __name__ == '__main__':
    print('Hello world')
    requests.packages.urllib3.disable_warnings()
    r = requests.put(url=api_url, headers=headers, data=json.dumps(request_data), verify=False)
    response = r.json()
    response_data = response[u'data']
    print(response_data)
