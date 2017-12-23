# -*- coding: utf-8 -*-
"""
Download file from web.
"""

import os
import os.path
from urllib.request import urlopen
# from urllib.request import urlretrieve
try:
    import wget
except ImportError:
    status = os.system('pip install wget')
    import wget


rar = 'http://www102.zippyshare.com/d/kbL2rs9I/12271/For.Dummies.Excel.VBA.Programming.For.Dummies.4th.Edition.1119077397.rar'
pdf = 'http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/dfztgh/201606/P020160622418453985437.pdf'
mp4 = ''
mp3 = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
pic = ''

"""
——————————————————————————————————————————————————————————————————————————————
use urlopen
——————————————————————————————————————————————————————————————————————————————
"""
def download(url):
    """输入文件url，下载该文件"""
    file_name = os.path.split(url)[1]
    file = urlopen(url)
    with open(file_name, 'wb') as f:
        f.write(file.read())
        print("文件下载成功：%s " % file_name)


"""
——————————————————————————————————————————————————————————————————————————————
use wget
——————————————————————————————————————————————————————————————————————————————
"""

filename = wget.download(pdf)

