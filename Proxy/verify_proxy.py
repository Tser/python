#! /usr/bin/env python
# coding=utf-8

import time, requests, urllib2

s = requests.session()
s.proxies = {
    'http': 'http://120.195.195.94:80',
    'https': 'https://120.195.195.94:80'
}
url = 'http://www.qq.com'
code = s.get(url, timeout=10).status_code  # 0.255999803543

# code = urllib2.urlopen(url).code        #0.0569999217987

if code == 200:
    print url, 'is OK'
else:
    print url, 'code:', code
print 'using time:', time.time() - stime
