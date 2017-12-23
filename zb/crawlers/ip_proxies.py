# -*- coding: utf-8 -*-
"""
IP代理自动获取，并检查可用性
"""

import requests
from zb_CodeSet.Spiders.url_downloader import download_with_requests
from bs4 import BeautifulSoup


"""
——————————————————————————————————————————————————————————————————————————————————————————
从xicidaili爬取免费代理
——————————————————————————————————————————————————————————————————————————————————————————
"""

def parser_xicidaili(xi_url):
    """解析xicidaili的url链接，获取可用的ip"""
    html = download_with_requests(xi_url)
    html = BeautifulSoup(html, 'lxml')

    ips = html.find('table', {'id': 'ip_list'})
    ips = ips.find_all('tr')
    ip_list = []
    for ip in ips[1:]:
        ip = [i.strip(' ') for i in ip.text.split('\n') if i != '']
        ip = ip[:2]
        ip_list.append(ip)
    return ip_list


def get_ips_from_xicidaili(page_num=3):
    """从xicidaili爬取免费代理(返回结果未验证可用性)"""
    url = 'http://www.xicidaili.com/nn/'
    ips = []
    for i in range(page_num):
        xi_url = url + str(i)
        try:
            ip_list = parser_xicidaili(xi_url)
            ips += ip_list
        except:
            continue
    return ips



"""
——————————————————————————————————————————————————————————————————————————————————————————
测试免费代理的可用性
——————————————————————————————————————————————————————————————————————————————————————————
"""
def is_usable(addr, port, timeout=3):
    """测试代理是否可用

    params
    ----------
    addr        ip地址
    port        端口号
    timeout     默认值为3，通过设置这个参数可以过滤掉一些速度慢的代理

    example
    ----------
    is_usable('222.180.24.13', '808', timeout=3)

    """
    try:
        proxies = {
            'http': 'http://%s:%s' % (addr, port),
            'https': 'https://%s:%s' % (addr, port)
        }
        requests.get('http://www.baidu.com/', proxies=proxies, timeout=timeout)
    except:
        print('failed: ', addr, port)
    else:
        print('success: ', addr, port)
        return addr, port


def check_ips(ips):
    """check all ip in ips, find usable ip"""
    ips_usable = []
    for ip in ips:
        # print(ip)
        try:
            addr, port = is_usable(ip[0], ip[1])
            ips_usable.append([addr, port])
        except:
            continue
    return ips_usable


"""
——————————————————————————————————————————————————————————————————————————————————————————
获取可用代理的主函数
——————————————————————————————————————————————————————————————————————————————————————————
"""
def get_IPs_in_xicidaili(page_num=3):
    """返回xicidaili中可用的ips"""
    ips = get_ips_from_xicidaili(page_num=page_num)  # len(ips)
    ips_usable = check_ips(ips)               # len(ips_usable)
    return ips_usable


if __name__ == "__main__":
    pass


