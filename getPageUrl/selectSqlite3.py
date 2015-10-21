#! /usr/bin/env python
#coding=utf-8

import sqlite3

sql_ser = sqlite3.connect('a_href.db')
sql_cu = sql_ser.cursor()
sql_cu.execute('select count(*) from baidu')
# sql_cu.execute('delete from dianping ')
# sql_ser.commit()
# sql_cu.execute('insert into dianping(netloc, url, status) values("www.dianping.com", "http://www.dianping.com/login", "OK")')
print sql_cu.fetchall()
sql_cu.close()
sql_ser.close()
