# -*- coding: utf-8 -*-

import os

try:
    import docx
except ImportError:
    os.system('pip install python-docx')

# 新建文档
doc_new = docx.Document()

# 读取文档
f = r'f:\Data_Warehouse\ProbeInfo\BaoAn_Sample\WangGe\共享库数据字典v1.3.docx'
doc = docx.Document(f)


