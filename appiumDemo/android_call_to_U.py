#! /usr/bin/env python
# coding=utf-8

'''
        platformName: MI NOTE
        Test android call...
        version=0.1
'''

from appium import webdriver
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '4.4'
caps['deviceName'] = ''
caps['appPackage'] = 'com.android.contacts'
caps['appActivity'] = '.activities.PeopleActivity'
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
driver.find_element_by_name(u'拨号').click()
call = driver.find_element_by_class_name('android.widget.Button')
assert call.get_attribute('text') == u'拨号'
call.click()
