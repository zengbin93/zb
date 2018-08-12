# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def pdf2text(path, password="", headers=None):
    """从pdf文件中提取文本

    :param path: str
        pdf文件在本地的地址或者url地址
    :param password: str
        pdf文件的打开密码，默认为空
    :param headers: dict
        请求url所需要的 header，默认值为 None
    :return: text
    """
    if path.startswith("http"):
        if headers:
            request = Request(url=path, headers=headers)
        else:
            request = Request(url=path, headers={})
        fp = urlopen(request)  # 打开在线PDF文档
    else:
        fp = open(path, 'rb')

    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize(password)

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        text = []
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    text.append(x.get_text())
    return text


