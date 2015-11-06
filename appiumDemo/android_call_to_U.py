#! /usr/bin/env python
# coding=utf-8

'''
        platformName: MI NOTE
        Test android call...
        version=0.1
'''
from appium import webdriver
from time import sleep
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '4.4'
caps['deviceName'] = ''
caps['appPackage'] = 'com.android.contacts'
caps['appActivity'] = '.activities.PeopleActivity'
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        # 元素属性text值唯一时，可以直接使用name来定位元素
        driver.find_element_by_name(u'拨号').click()
        # 元素text值不唯一时，可以通过className的值来定位（定位好className，判断属性值是否为某一特定的值）
        call = driver.find_element_by_class_name('android.widget.Button')
        assert call.get_attribute('text') == u'拨号'
        call.click()
except Exception, e:
        print e.message
finally:
        sleep(5)  # 为了查看结果...
        # 执行此语句，为了结束本次对话(即：session)，方便下次执行脚本不用重新启动appium服务
        driver.quit()
