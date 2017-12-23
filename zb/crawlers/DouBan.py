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
from PIL import Image

from zb_CodeSet.Spiders.utils import get_header

"""
————————————————————————————————————————————————————————————————————————————————————————
模拟登陆
1. use post
2. use cookies
————————————————————————————————————————————————————————————————————————————————————————
"""


def login_with_post(user, pw):
    """模拟登录：使用post方法传递用户名和密码"""
    session = requests.Session()
    session.headers.update(get_header())

    # 构造登录需要的信息
    data = {
        'source': 'index_nav',
        'redir': 'http://www.douban.com',
        'form_email': user,
        'form_password': pw,
        'login': '登录',
    }

    # 获取验证码
    url = 'https://accounts.douban.com/login'
    html = requests.get(url)
    html = BeautifulSoup(html.text, 'lxml')
    caprcha_link = html.select('#captcha_image')[0]['src']
    caprcha_id = html.select('div.captcha_block > input')[1]['value']
    fn_jpg = 'caprcha.jpg'
    if caprcha_id:  # 如果有caprcha_id,就执行解析caprcha_link网页信息，并把图片保存下来打开
        img_html = session.get(caprcha_link)
        with open(fn_jpg, 'wb') as f:
            f.write(img_html.content)
        try:
            im = Image.open(fn_jpg)
            im.show()
            im.close()
            os.remove(fn_jpg)
        except:
            print('打开错误')
        caprcha = input('请输入验证码：')  # 把看到的验证码图片输入进去

    if caprcha_id:  # 如果需要验证码就把下面的两个数据加入到data里面
        data['captcha-id'] = caprcha_id
        data['captcha-solution'] = caprcha

    # 登录
    session.post(url, data=data)
    if session.cookies:
        print(' %s 登录成功！\n cookies： ' % user, session.cookies.items())
    else:
        print('%s 登录失败，请重试！' % user)

    return session


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


def parse_douban_group(session, page1):
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


def parse_douban_read():
    # 拼接urls（所有url）
    urls = []
    for i in (0, 10, 20):
        urls.append('https://read.douban.com/search?q=PYTHON&start=' + str(i))
    print(urls)

    for url in urls:
        # 读取网页内容
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req).read().decode('utf-8')
        # 解析网页
        soup = BeautifulSoup(res, 'lxml')
        # 循环的方式读取所需字段
        for content in soup.select('.info'):
            title = content.select('.title')[0].text
            if not content.select('.author-item'):
                anthor = None
            else:
                author = content.select('.author-item')[0].text
            price = content.select('.price-tag')[0].text
            category = content.select('.category')[0].text[3:]
            if not content.select('.rating-average'):
                rating = None
            else:
                rating = content.select('.rating-average')[0].text
            if not content.select('.ratings-link'):
                eveluate_nums = None
            else:
                eveluate_nums = content.select('.ratings-link')[0].text[:-3]
            if not content.select('.article-desc-brief'):
                desc = None
            else:
                desc = content.select('.article-desc-brief')[0].text
            print(title, author, price, category, rating, eveluate_nums, desc)
