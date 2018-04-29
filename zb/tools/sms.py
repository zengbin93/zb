# -*- coding: utf-8 -*-
"""
——————————————————————————————————————————————————————————————————————————————————————————
Send Message Service
——————————————————————————————————————————————————————————————————————————————————————————
"""


from retrying import retry
import os


"""
——————————————————————————————————————————————————————————————————————————————————————————
使用server酱推送消息
——————————————————————————————————————————————————————————————————————————————————————————
"""


import requests

@retry(stop_max_attempt_number=6)
def push_sms(title, content, key):
    """使用server酱推送消息到微信"""
    # post方法推送
    url = 'https://sc.ftqq.com/%s.send' % key
    requests.post(url, data={'text': title, 'desp': content})


"""
——————————————————————————————————————————————————————————————————————————————————————————
邮件发送模块，支持发送附件。
——————————————————————————————————————————————————————————————————————————————————————————
"""

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    """
    example
    ----------------
    subject = '附件发送测试'
    content = '检测附件发送是否成功'
    files = ['test.py',
             'f:\\已下载.txt']

    e = EmailSender('zeng_bin8888@163.com', pw=pw, service='163')
    e.send_email(to, subject, content, files)
    """
    def __init__(self, from_, pw, service='qq'):
        self.from_ = from_  # 用于发送email的邮箱
        self.pw = pw        # 发送email的邮箱密码
        self.smtp = smtplib.SMTP()
        if service == 'qq':
            self.smtp.connect('smtp.exmail.qq.com')
            self.smtp.login(self.from_, self.pw)
        elif service == '163':
            self.smtp.connect('smtp.163.com')
            self.smtp.login(self.from_, self.pw)
        else:
            print('目前仅支持163和qq邮箱！')


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


    @retry(stop_max_attempt_number=6)
    def send_email(self, to, subject, content, files=None):
        """登录邮箱，发送msg到指定联系人

        :param to: str: 收件人邮箱
        :param subject: str: 主题
        :param content: str: 内容
        :param files:  list: 附件列表
        :return: None
        """
        smtp = self.smtp
        msg = EmailSender._construct_msg(self, to, subject, content, files=files)
        smtp.sendmail(self.from_, to, str(msg))


    def quit(self):
        smtp = self.smtp
        smtp.quit()  # 退出登录
