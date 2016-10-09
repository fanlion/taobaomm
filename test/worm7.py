#!/usr/bin/env python
#-*-coding:utf-8-*-

""" response的geturl方法使用, 利用该方法查看真实访问的url，可以查看到跳转后真实访问的地址"""

import urllib2

old_url = 'http://rrurl.cn/b1UZuP'
req = urllib2.Request(old_url)
reponse = urllib2.urlopen(req)

real_url = reponse.geturl()
print 'Old url: ', old_url
print 'Real url: ', real_url