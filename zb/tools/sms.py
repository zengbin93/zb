# -*- coding: utf-8 -*-
"""
Send Message Service
====================================================================
"""
import traceback
import requests
import os
import functools
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def server_chan_push(title, content, key=None):
    """使用server酱推送消息到微信，关于server酱，
    请参考：http://sc.ftqq.com/3.version

    :param title: str
        消息标题
    :param content: str
        消息内容，最长64Kb，可空，支持MarkDown
    :param key: str
        从[Server酱](https://sc.ftqq.com/3.version)获取的key
    :return: None
    """
    if not key:
        raise ValueError("请配置key，如果还没有key，"
                         "可以到这里申请一个：http://sc.ftqq.com/3.version")
    url = 'https://sc.ftqq.com/%s.send' % key
    requests.post(url, data={'text': title, 'desp': content})


def bear_push(title, content, send_key=None):
    """使用PushBear推送消息给所有订阅者微信，关于PushBear，
    请参考：https://pushbear.ftqq.com/admin/#/

    :param title: str
        消息标题
    :param content: str
        消息内容，最长64Kb，可空，支持MarkDown
    :param send_key: str
        从[PushBear](https://pushbear.ftqq.com/admin/#/)获取的通道send_key
    :return: None
    """
    if not send_key:
        raise ValueError("请配置通道send_key，如果还没有，"
                         "可以到这里创建通道获取：https://pushbear.ftqq.com/admin/#/")
    api = "https://pushbear.ftqq.com/sub"
    requests.post(api, data={'text': title, 'desp': content, "sendkey": send_key})


def push2wx(send_key, by="bear"):
    """装饰器：推送消息到微信

    :param send_key: str
        用于发送消息的key
    :param by: str 默认值 bear
        发送消息的方式，默认是bear，
        可选值 ['bear', 'server_chan']
    :return:
    """
    def _wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            title, content = func(*args, **kw)
            if by == "bear":
                bear_push(title, content, send_key=send_key)
            elif by == "server_chan":
                server_chan_push(title, content, key=send_key)
            else:
                raise ValueError("参数by的可选值为 ['bear', 'server_chan']")
            return title, content
        return wrapper
    return _wrapper


class EmailSender:
    def __init__(self, from_, pw, service='qq'):
        self.from_ = from_  # 用于发送email的邮箱
        self.pw = pw  # 发送email的邮箱密码
        self.service = service
        self.smtp = smtplib.SMTP()
        self.login()

    def login(self):
        if self.service == 'qq':
            self.smtp.connect('smtp.exmail.qq.com')
            self.smtp.login(self.from_, self.pw)
        elif self.service == '163':
            self.smtp.connect('smtp.163.com')
            self.smtp.login(self.from_, self.pw)
        else:
            raise ValueError('目前仅支持163和qq邮箱！')

    def _construct_msg(self, to, subject, content, files=None):
        """构造email信息

        parameters
        ---------------
        subject     邮件主题
        content     邮件文本内容
        files       附件（list）
                    可以是相对路径下的文件，也可以是绝对路径下的文件；
                    推荐使用绝对路径。

        return
        --------------
        msg         构造好的邮件信息
        """
        msg = MIMEMultipart()
        msg['from'] = self.from_
        msg['to'] = to
        msg['subject'] = subject
        txt = MIMEText(content)
        msg.attach(txt)

        # 添加附件
        if files is not None:
            for file in files:
                f = MIMEApplication(open(file, 'rb').read())
                f.add_header('Content-Disposition', 'attachment',
                             filename=os.path.split(file)[-1])
                msg.attach(f)

        return msg

    def send_email(self, to, subject, content, files=None):
        """登录邮箱，发送msg到指定联系人

        :param to: str: 收件人邮箱
        :param subject: str: 主题
        :param content: str: 内容
        :param files:  list: 附件列表
        :return: None
        """
        msg = EmailSender._construct_msg(self, to, subject, content, files=files)
        try:
            self.smtp.sendmail(self.from_, to, str(msg))
        except:
            traceback.print_exc()
            self.login()
            self.smtp.sendmail(self.from_, to, str(msg))

    def quit(self):
        self.smtp.quit()  # 退出登录


def send_email(sender, pw, to, subject, content, files=None, service='163'):
    """send email, recommended use 163 mailbox service, as it is tested.

    :param sender: str
        email address of sender
    :param pw: str
        password for sender
    :param to: str
        email addressee
    :param subject: str
        subject of email
    :param content: str
        content of email
    :param files: list
        path list of attachments
    :param service: str
        smtp server address, optional is ['163', 'qq']
    :return: None
    """
    se = EmailSender(from_=sender, pw=pw, service=service)
    se.send_email(to=to, subject=subject, content=content, files=files)
    se.quit()
