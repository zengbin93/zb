# -*- coding: utf-8 -*-

"""
————————————————————————————————————————————————————————————————————————————————————————
豆瓣网爬虫

————————————————————————————————————————————————————————————————————————————————————————
"""

import os
import requests
import urllib
from bs4 import BeautifulSoup

from .utils import get_header

"""
————————————————————————————————————————————————————————————————————————————————————————
模拟登陆
1. use post
2. use cookies
————————————————————————————————————————————————————————————————————————————————————————
"""


def login_with_cookies(raw_cookies):
    """创建cookies

    example
    -----------
    raw_cookies = 'bid=tiyTMxpIffk; ll="118282"; ps=y; ue="1257391203@qq.com"; dbcl2="143012014:C8XrOzYKwJc"; push_noty_num=0; push_doumail_num=0; __ads_session=cfktlbLf+Ags5WswgQA=; ck=FBAI; ap=1'
    session = login_with_cookies(raw_cookies)
    """
    cookies = {}
    for line in raw_cookies.split(';'):
        key, value = line.split('=', 1)
        cookies[key.strip(' ')] = value

    session = requests.Session()
    session.cookies.update(cookies)
    session.headers.update(get_header())

    return session


"""
————————————————————————————————————————————————————————————————————————————————————————
豆瓣小组
————————————————————————————————————————————————————————————————————————————————————————
"""


def parse_group(session, page1):
    # page1 = 'https://www.douban.com/group/'
    group = session.get(page1)
    soup = BeautifulSoup(group.text, 'lxml')
    titles = soup.select('tr.pl > td.td-subject > a.title')
    for title in titles:
        print(title['href'], title.string)
    return titles


"""
————————————————————————————————————————————————————————————————————————————————————————
豆瓣阅读
https://read.douban.com/search?q=Python&start=
————————————————————————————————————————————————————————————————————————————————————————
"""
