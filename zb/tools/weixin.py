# -*- coding: utf-8 -*-

from wxpy import *

# 扫码登陆微信网页版
bot = Bot()  # 退出登录 bot.logout()

# 好友列表
friends = [str(f).strip('<Friend: >') for f in list(bot.friends())]

# 获取一个friend对象
my_friend = bot.friends().search('宋庆星')[0]


# 群列表
groups = [str(g).strip('<Group: >') for g in list(bot.groups())]

# 获取一个group对象
ng_group = bot.groups().search('Andrew ng Deep learning')[0]


sent_msgs = bot.messages


print(sent_msgs)

