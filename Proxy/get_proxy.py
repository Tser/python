#! /usr/bin/env python
# coding=utf-8

from ghost import Ghost
import stackless

ghost = Ghost()

with ghost.start() as session:
    page, = session.open('http://www.oschina.net/project/tag/216/ostools?lang=0&os=0&sort=view&p=1')
    assert page.http_status == 200 and 'bootin' in page.content
