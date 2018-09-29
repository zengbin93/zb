# -*- coding: utf-8 -*-
"""
zb.nlp.kwe - 关键词提取

kwe = key word extract
====================================================================
"""


import jieba.analyse
from textrank4zh import TextRank4Keyword


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
