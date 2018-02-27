# -*- coding: utf-8 -*-

"""
======================================================================================
ftp server

if pyftpdlib is not installed, install it first! (pip install pyftpdlib)

reference: http://www.cnblogs.com/huangxm/p/6274645.html


读权限 ：
e 	改变文件目录
l 	列出文件
r 	从服务器接收文件

写权限 ：
a 	文件上传
d 	删除文件
f 	文件重命名
m 	创建文件
w 	写权限
M 	文件传输模式（通过FTP设置文件权限 ）
======================================================================================
"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
import logging

"""
======================================================================================
setting
======================================================================================
"""


class settings:
    ip = None
    if not ip:
        ip

    port = '21'

    user_list = [
        # 用户名   密码       权限       目录
        ['root', '12345', 'elradfmwM', 'C:\ZB'],
    ]

    # 上传速度  300kb/s
    max_upload = 3000 * 1024

    # 下载速度 300kb/s
    max_download = 3000 * 1024

    # 最大连接数
    max_cons = 150

    # 最多IP数
    max_per_ip = 10

    # 被动端口范围，注意被动端口数量要比最大IP数多，否则可能出现无法连接的情况
    passive_ports = (2000, 2200)

    # 是否开启匿名访问 on|off
    enable_anonymous = 'off'

    # 匿名用户目录
    anonymous_path = ''

    # 是否开启日志 on|off
    enable_logging = 'on'
    # 日志文件
    logging_name = './pyftp.log'

    # 欢迎信息
    welcome_msg = 'Welcome to my ftp'


def ftp_server():
    # 实例化虚拟用户，这是FTP验证首要条件
    authorizer = DummyAuthorizer()

    for user in settings.user_list:
        name, passwd, permit, homedir = user
        try:
            authorizer.add_user(name, passwd, homedir, perm=permit)
        except Exception as e:
            print(e)

    # 添加匿名用户 只需要路径
    if settings.enable_anonymous == 'on':
        authorizer.add_anonymous(settings.anonymous_path)

    # 下载上传速度设置
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = settings.max_download
    dtp_handler.write_limit = settings.max_upload

    # 初始化ftp句柄
    handler = FTPHandler
    handler.authorizer = authorizer

    # 日志记录
    if settings.enable_logging == 'on':
        logging.basicConfig(filename=settings.logging_name, level=logging.INFO)

    # 欢迎信息
    handler.banner = settings.welcome_msg

    # 添加被动端口范围
    handler.passive_ports = range(settings.passive_ports[0], settings.passive_ports[1])

    # 监听ip 和 端口
    server = FTPServer((settings.ip, settings.port), handler)

    # 最大连接数
    server.max_cons = settings.max_cons
    server.max_cons_per_ip = settings.max_per_ip

    # 开始服务
    server.serve_forever()


if __name__ == "__main__":
    ftp_server()
