# coding: utf-8
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "..")
from zb.wx.qy import GroupMessenger


def test_group_messenger():
    key = "13c84e2a-9201-463c-8e52-30f73e620e50"
    group_messenger = GroupMessenger(key)

    file_img = "./data/1.jpg"
    # group_messenger.push_image(file_img)
    file = './data/x.xlsx'
    group_messenger.push_file(file)

    group_messenger.push_text(msg_type='markdown', content={"content": "# 测试一下"})
    group_messenger.push_text(msg_type='text', content={"content": "# 测试一下"})


