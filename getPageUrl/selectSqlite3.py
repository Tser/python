#! /usr/bin/env python
#coding=utf-8

import sqlite3, re

sql_ser = sqlite3.connect('a_href.db')
sql_cu = sql_ser.cursor()
sql_cu.execute('select * from baidu')
# # sql_cu.execute('delete from baidu ')
sql_ser.commit()
print sql_cu.fetchall()
sql_cu.close()
sql_ser.close()
