# -*- coding: utf-8 -*-
"""
zb.nlp.kwe - 关键词提取

kwe = key word extract
====================================================================
"""


import jieba.analyse
from textrank4zh import TextRank4Keyword

#
# text = '6月19日,《2012年度“中国爱心城市”公益活动新闻发布会》在京举行。' + \
#        '中华社会救助基金会理事长许嘉璐到会讲话。基金会高级顾问朱发忠,全国老龄' + \
#        '办副主任朱勇,民政部社会救助司助理巡视员周萍,中华社会救助基金会副理事长耿志远,' + \
#        '重庆市民政局巡视员谭明政。晋江市人大常委会主任陈健倩,以及10余个省、市、自治区民政局' + \
#        '领导及四十多家媒体参加了发布会。中华社会救助基金会秘书长时正新介绍本年度“中国爱心城' + \
#        '市”公益活动将以“爱心城市宣传、孤老关爱救助项目及第二届中国爱心城市大会”为主要内容,重庆市' + \
#        '、呼和浩特市、长沙市、太原市、蚌埠市、南昌市、汕头市、沧州市、晋江市及遵化市将会积极参加' + \
#        '这一公益活动。中国雅虎副总编张银生和凤凰网城市频道总监赵耀分别以各自媒体优势介绍了活动' + \
#        '的宣传方案。会上,中华社会救助基金会与“第二届中国爱心城市大会”承办方晋江市签约,许嘉璐理' + \
#        '事长接受晋江市参与“百万孤老关爱行动”向国家重点扶贫地区捐赠的价值400万元的款物。晋江市人大' + \
#        '常委会主任陈健倩介绍了大会的筹备情况。'


def kwe_by_tfidf(text, top=10, pos=None, with_weight=False):
    """

    :param text:
    :param top:
    :param pos:
    :param with_weight:
    :return:
    """
    if pos is None:
        pos = ['ns', 'n', 'vn', 'v', 'nr']
    kw = jieba.analyse.extract_tags(text, topK=top, withWeight=True,
                                    allowPOS=pos)
    if not with_weight:
        kw = [x[0] for x in kw]
    return kw


def kwe_by_textrank(text, top=10, pos=None, with_weight=False, key_phrase=False):
    """

    :param text:
    :param top:
    :param pos:
    :param with_weight:
    :param key_phrase:
    :return:
    """
    if pos is None:
        pos = ['ns', 'n', 'vn', 'v', 'nr']
    tr4k = TextRank4Keyword(allow_speech_tags=pos)
    tr4k.analyze(text)
    kw = tr4k.get_keywords(num=top, word_min_len=2)
    if not with_weight:
        kw = [x['word'] for x in kw]
    else:
        kw = [(x['word'], x['weight']) for x in kw]

    if key_phrase:
        kp = tr4k.get_keyphrases(keywords_num=top, min_occur_num=2)
        return kw, kp
    else:
        return kw
