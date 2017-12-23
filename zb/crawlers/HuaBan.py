# -*- coding: utf-8 -*-
"""
————————————————————————————————————————————————————————————————————————————————————————
花瓣网爬虫 -- 批量获取美图

页面分析：
1、home  http://huaban.com/
2、http://huaban.com/discovery/
3、http://huaban.com/pins/68106074/

————————————————————————————————————————————————————————————————————————————————————————
"""



# import requests
from selenium import webdriver
from urllib.request import quote
from urllib.request import urlopen
from zb_CodeSet.Spiders.utils import get_header
from bs4 import BeautifulSoup
import requests


img = 'http:' + '//img.hb.aicdn.com/5a94edc3a30607dcc881af5d7a9c2d696b16203d29407-8fOTcH_fw658'

def save_pic(img_url, name):
    """保存图片"""
    pic = urlopen(img_url)
    with open(name, 'wb') as f:
        f.writelines(pic.readlines())


def search_url(key='笑', sort=None):
    """花瓣搜索，下载图片

    params
    ---------
    key     str
            搜索关键词，如：‘笑’
    sort    weight, relative, created_at  默认 None
            搜索结果的排序方法
            None = 综合
            weight = 热门
            relative = 匹配度
            created_at = 时间
    """
    if sort is None:
        url = 'http://huaban.com/search/?q=' + quote(key)
    else:
        url = 'http://huaban.com/search/?q=' + quote(key) + '&sort=' + sort

    return url


def download_url(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    return bsObj
