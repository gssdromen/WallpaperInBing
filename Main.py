# coding=utf-8

from datetime import date
import urllib
import re
import time
def getHtml(url):
    return urllib.urlopen(url).read()

def getImgUrl(html):
    reg=re.compile(r'(http://s.cn.bing.net/.*?\.jpg)') #正则式
    url=reg.findall(html)
    print url[0]
    return url[0]

def downloadImg(url,path):
    today = date.today().isoformat()
    xpath=path+'\\'+today+'.jpg'
    print xpath
    urllib.urlretrieve(url,xpath)

if __name__=='__main__':
    start=time.time()
    html=getHtml('http://cn.bing.com/')
    url=getImgUrl(html)
    downloadImg(url,'wallpapers')
    end=time.time()