#!/usr/bin/env python
#-*-coding:utf-8-*-

"""添加header信息到请求中"""

import urllib
import urllib2

url = 'http://www.baidu.com/'
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'lifan',
         'location' : 'SDU',
         'language' : 'Python'}

headers = {'User-Agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print  the_page