#!/usr/bin/env python
#-*-coding:utf-8-*-


""" response的info方法使用，利用该方法可以查看到所访问页面的headers消息 """
import urllib2


old_url = 'http://www.baidu.com/'
req = urllib2.Request(old_url)
response = urllib2.urlopen(req)

print 'Info():'
print response.info()