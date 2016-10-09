#!/usr/bin/env python
#-*-coding:utf-8-*-

"""get方式带数据提交表单"""

import urllib
import urllib2

data = {}

data['name'] = '李繁'
data['location'] = 'sdu'
data['language'] = 'Python'

url_values = urllib.urlencode(data)
print 'before encode url:', url_values

url = 'http://www.baidu.com/'
full_url = url + '?' + url_values

print 'after encode url:', full_url