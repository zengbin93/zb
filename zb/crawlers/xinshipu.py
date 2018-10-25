# -*- coding: utf-8 -*-
"""
心食谱 爬虫

https://www.xinshipu.com/
====================================================================
"""

import requests
from bs4 import BeautifulSoup
import re

from zb.crawlers.utils import get_header

HOME_URL = "https://www.xinshipu.com/"


def get_recipe_detail(recipe_url):
    """从url中获取菜谱详细信息

    :param recipe_url: str
        菜谱url，如：https://www.xinshipu.com/zuofa/598775
    :return:dict
    """
    # recipe_url = "https://www.xinshipu.com/zuofa/598775"
    response = requests.get(recipe_url, headers=get_header())
    html = BeautifulSoup(response.text, 'lxml')

    # 获取菜名
    name = html.find("div", {"class": "re-up"}).h1.text

    all_info = html.find_all("div", {"class": "dd"})

    # 简介
    intro = re.sub('\n|\t|\r| ', '', all_info[0].text)

    # 食材
    material = all_info[1].text.strip()
    material = re.sub('\r\n|\r\n \n', '\n', material)

    # 做法
    method = all_info[2].text.strip()
    method = re.sub('\r\n|\r\n \n', '\n', method)

    # 相关菜品
    classify = all_info[4].text.strip().replace('\xa0\xa0', ' | ')

    return {
        "name": name,
        "url": recipe_url,
        "intro": intro,
        "material": material,
        "method": method,
        "classify": classify
    }


def get_all_classify():
    """获取全部菜谱分类"""
    url = "https://www.xinshipu.com/%E8%8F%9C%E8%B0%B1%E5%A4%A7%E5%85%A8.html"
    response = requests.get(url, headers=get_header())
    html = BeautifulSoup(response.text, "lxml")

    all_a = html.find("div", {'class': "detail-cate-list clearfix mt20"}).find_all('a')
    classify = dict()

    for a in all_a:
        if a.has_attr('rel') and not a.has_attr('class'):
            class_url = HOME_URL + a['href']
            classify[a.text] = class_url

    return classify


def get_class_recipes(class_url):
    """获取某个菜谱分类url下的所有菜谱url"""
    class_url = class_url + "?page={page}"
    recipes = dict()

    # 暴力爬取方案，每个菜谱分类请求100页
    for page in range(1, 100):
        url = class_url.format(page=page)
        print("current url: ", url)
        response = requests.get(url, headers=get_header())
        html = BeautifulSoup(response.text, "lxml")

        # 获取本页菜谱
        menus = html.find("div", {'class': 'new-menu-list search-menu-list clearfix mt10'})
        if menus:
            menus = menus.find_all('a')
            for m in menus:
                name = re.sub("\n| ", "", m.text)
                recipe_url = HOME_URL + m['href']
                recipes[name] = recipe_url

        # 判断是否是最后一页
        # next_page = html.find('div', {'class': 'paging mt20'}).text
        # if "下一页" in next_page:
        #     page += 1
        # else:
        #     break
    return recipes


if __name__ == '__main__':
    import json
    import os
    data_path = r"C:\ZB\git_repo\recipes"

    # 分类url
    file_classify = os.path.join(data_path, "classify_url.json")
    if os.path.exists(file_classify):
        classify = json.load(open(file_classify, 'r', encoding='utf-8'))
    else:
        classify = get_all_classify()
        json.dump(classify, open(file_classify, 'w', encoding='utf-8'),
                  indent=2, ensure_ascii=False)

    # 食谱url
    file_recipes = os.path.join(data_path, "recipes_url.json")
    if os.path.exists(file_recipes):
        recipes_url = json.load(open(file_recipes, 'r', encoding='utf-8'))
    else:
        recipes_url = dict()
        for class_url in classify.values():
            class_recipes = get_class_recipes(class_url)
            recipes_url.update(class_recipes)
        json.dump(recipes_url, open(file_recipes, 'w', encoding='utf-8'),
                  indent=2, ensure_ascii=False)

    # 食谱详细信息
    file_recipes_detail = os.path.join(data_path, "recipes_detail.json")
    if os.path.exists(file_recipes_detail):
        recipes_detail = json.load(open(file_recipes_detail, 'r'))
    else:
        recipes_detail = dict()
    for recipe_url in recipes_url:
        if recipe_url in recipes_detail.keys():
            continue
        print("current: ", recipe_url)
        detail = get_recipe_detail(recipe_url)
        recipes_detail[recipe_url] = detail







