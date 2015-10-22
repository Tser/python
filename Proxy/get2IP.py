#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
			抓取(国外)代理IP
'''

import requests, os, socket, string, time
from pyquery import PyQuery as pq

db = []
baseUrl = 'http://www.xicidaili.com/wn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/43.0.2357.132 Safari/537.36'
}
HTML = requests.get(baseUrl, headers=headers).content
print u'TIME:', time.ctime()
for td in pq(HTML).find("td"):
    db.append(pq(td).text())
    for index in range(len(db)):
        if db[index].find(".") != -1:
            if os.popen('ping ' + db[index]).read().find("TTL") != -1:  # 只保证能ping通
                try:
                    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    if soc.connect((db[index], string.atoi(db[index + 1]))) != None:  # 保证ip及端口能够正常连接
                        print u"此ip可以使用：", \
                            db[index], \
                            db[index + 1], \
                            db[index + 2], \
                            db[index + 3], \
                            db[index + 4], \
                            db[index + 5]
                except:
                    pass
