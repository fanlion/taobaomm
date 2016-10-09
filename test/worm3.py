#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib
import urllib2

url = 'http://www.baidu.com/'

values = {'name' : 'lifan',
          'location' : 'SDU',
          'language' : 'Python'}

data = urllib.urlencode(values) #编码工作
req = urllib2.Request(url, data) #发送请求时同传data表单
response = urllib2.urlopen(req) #接收反馈信息
the_page = response.read() #打印html

print the_page
