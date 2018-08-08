# -*- coding: utf-8 -*-
"""
IP代理自动获取，并检查可用性
====================================================================
"""

import requests
from urllib.error import HTTPError


# 测试代理是否可用
# --------------------------------------------------------------------

def is_usable(host, port, timeout=3):
    """测试代理是否可用

    params
    ----------
    host        ip地址
    port        端口号
    timeout     默认值为3，通过设置这个参数可以过滤掉一些速度慢的代理

    example
    ----------
    is_usable('222.180.24.13', '808', timeout=3)

    """
    try:
        proxies = {
            'http': 'http://%s:%s' % (host, port),
            'https': 'https://%s:%s' % (host, port)
        }
        requests.get('http://www.baidu.com/', proxies=proxies, timeout=timeout)
    except HTTPError:
        print('failed: ', host, port)
        return False
    else:
        print('success: ', host, port)
        return True
