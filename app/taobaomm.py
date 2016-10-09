#!/usr/bin/dev python
#-*- coding:utf-8-*-


"""
文件用于爬取https://mm.taobao.com/json/request_top_list.htm?page=1
上的data-userid数据，该字段为淘宝MM的用户id，利用该id可以访问淘宝MM们的主页，从而可以
从主页抓取照片


https://mm.taobao.com/self/aiShow.htm?userId=646858747
上述url为访问淘宝MM主页的链接

此程序用于保存上述的userid

author:李繁
date:2016年10月8日10:22:15
"""



import urllib2
import urllib
import re

def get_userid(url):

    """用于请求一个url，并利用正则表达式从获取到的html页面中得到userid"""

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_html = response.read() #获取HTML
    userid_re = re.compile('data-userid=\"(\d{4,9})\"') ##网页中的userid表现形式为(data-userid='213808410')
    result = userid_re.findall(the_html)
    return result

def save_userid(data, file):

    """用于保存userid到指定文件中"""

    f = open(file, 'a')
    for x in data:
        f.write(x + '\n')
    f.close()


def main():

    """ 程序入口"""

    url = 'https://mm.taobao.com/json/request_top_list.htm?page='
    cnt = 1
    file = "D:\\userid.txt"
    while cnt < 1000:
        data = get_userid(url + str(cnt))
        save_userid(data, file)
        cnt += 1
        print '正在保存第%s页..........' % cnt
    print '保存成功..............................'

if __name__ == '__main__':
    main()