#!/usr/bin/env python
#-*-coding:utf-8-*-

"""如何利用urllib2抓取一个网页的HTML"""

import urllib2

response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
print html