#! /usr/bin/env python
# coding=utf-8

import time, requests, urllib2

stime = time.time()

url = 'http://www.qq.com'
code = requests.get(url).status_code  # 0.255999803543

# code = urllib2.urlopen(url).code        #0.0569999217987

if code == 200:
    print url, 'is OK'
else:
    print url, 'code:', code
print 'using time:', time.time() - stime
