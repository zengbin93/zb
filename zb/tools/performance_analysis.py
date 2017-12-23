# -*- coding: utf-8 -*-

import functools
import time


def time_cost(func):
    """装饰器：计算函数运行耗时"""
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        print('正在运行函数 %s() ...' % func.__name__)
        res = func(*args, **kw)
        end = time.time()
        print('函数【 %s() 】运行耗时：%.2f 秒' % (func.__name__, end - start))
        return res
    return wrapper
