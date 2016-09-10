#!/usr/bin/python
# coding=utf-8

from datetime import date
import urllib
import re
import time
import os
import sys

def getHtml(url):
    return urllib.urlopen(url).read()

def getImgUrl(html):
    reg=re.compile(r'(http://s.cn.bing.net/.*?\.jpg)') #正则式
    url=reg.findall(html)
    print url[0]
    return url[0]

def downloadImg(url,path):
    today = date.today().isoformat()
    xpath = os.path.join(path, today+'.jpg')
    # xpath=path+'/'+today+'.jpg'
    print xpath
    urllib.urlretrieve(url,xpath)

    #获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

if __name__=='__main__':
    start=time.time()
    html=getHtml('http://cn.bing.com/')
    url=getImgUrl(html)
    downloadImg(url,os.path.join(cur_file_dir(),'wallpapers'))
    end=time.time()
