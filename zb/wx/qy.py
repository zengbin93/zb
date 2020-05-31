# coding: utf-8
import requests
from hashlib import md5
import base64
import os


class GroupMessenger:
    """群聊机器人"""

    def __init__(self, key):
        """
        群机器人配置说明: https://work.weixin.qq.com/api/doc/90000/90136/91770

        :param key:
        """
        self.key = key
        self.api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}".format(key=key)

    def _post(self, data):
        response = requests.post(self.api, json=data)
        assert response.json()['errmsg'] == 'ok', str(response.json())
        return response

    def push_text(self, msg_type, content):
        """推送消息"""
        data = {"msgtype": msg_type, msg_type: content}
        return self._post(data)

    def push_image(self, image):
        """推送图片"""
        with open(image, 'rb') as f:
            img = f.read()

        m = md5()
        m.update(img)
        image_md5 = m.hexdigest()

        b = base64.b64encode(img)
        image_base64 = b.decode()
        data = {
            "msgtype": "image",
            "image": {
                "base64": image_base64,
                "md5": image_md5
            }
        }
        return self._post(data)

    def push_file(self, file):
        """推送文件"""
        raise NotImplementedError
        # key = self.key
        #
        # ext = os.path.splitext(file)
        # print(ext)
        # if len(ext) > 1:
        #     ext = ext[1][1:]
        #     if ext.lower() in ['jpg', 'png', 'bmp']:
        #         file_type = 'image'
        #         content_type = '{}/{}'.format(file_type, ext)
        #     elif ext.lower() in ['amr', 'mp3']:
        #         file_type = 'voice'
        #         content_type = '{}/{}'.format(file_type, ext)
        #     elif ext.lower() in ['mp4']:
        #         file_type = 'video'
        #         content_type = '{}/{}'.format(file_type, ext)
        #     else:
        #         file_type = 'file'
        #         content_type = 'application/octet-stream'
        # else:
        #     file_type = 'file'
        #     content_type = 'application/octet-stream'
        #
        # upload_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media" \
        #              "?key={key}&type={file_type}".format(key=key, file_type=file_type)
        #
        # files = {'file': (file, open(file, 'rb'), content_type, {'Expires': '0'})}
        #
        # data = requests.post(upload_api, files=files).json()
        # print(data)
        # assert data['errmsg'] == 'ok', str(data)
        # data.pop('errmsg')
        # data.pop('errcode')
        # print(data)
        # return self._post(data)


