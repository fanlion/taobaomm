#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
import urllib
import re
import os

""" 获取图片"""

def get_pic(userid, dir):

    """根据用户id下载该用户主页的所有图片"""

    image_url = "https://mm.taobao.com/self/aiShow.htm?userId=" + userid #用户主页的url
    response = urllib2.urlopen(image_url)
    the_page = response.read().decode('gbk') #解码，避免中文乱码
    re_s = r'src="//(img.alicdn.com/.+?\.jpg)"' #正则表达式，获取图片地址(img.alicdn.com/imgextra/开头,.jpg结尾）

    pic_re = re.compile(re_s)
    result = re.findall(pic_re, the_page)
    cnt = 1
    print '开始下载用户id为%s的照片....' % userid
    path = dir + str(userid)  # 以用户id创建一个目录用于保存该用户的照片
    flag = mkdir(path)  # 创建目录

    #获取该用户的所有图片链接并下载图片保存至本地
    for item in result:
        try:
            filename = path + '//' + str(cnt) + '.jpg'
            print filename
            urlhandler = urllib.URLopener()
            urlhandler.retrieve('https://' + item, filename)
            cnt += 1
            print '正在下载第%s照片....' % str(cnt)
        except:
            continue

def mkdir(path):

    """ 创建一个目录"""

    path = path.strip() #去除首位空格
    path = path.rstrip('\\') #去除尾部\符号
    #判断路径是否存在
    #存在  True
    #不存在 False
    isExists = os.path.exists(path)

    #判断结果
    if not isExists:
        #不存在则创建目录
        print path + ' 创建成功'
        os.makedirs(path)
        return True
    else:
        print path + ' 目录已经存在'
        return False






def main(file):

    """主函数入口"""

    #从保存有userid的文件中每次读取一个用户id，然后获取该用户id主页中的图片
    f = open(file, 'r')
    i = 1
    for userid in f:
        #获取该id的图片
        get_pic(userid.strip('\n'), 'D://taobao//') #去掉换行符并开始执行
    f.close()
    print '已经获取所有%s文件中id的图片...........................................................' % file




if __name__ == '__main__':
    main('D:\\userid.txt')