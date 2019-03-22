# -*- coding: utf-8 -*-

import os
import PyPDF2


def merge_pdf(pdf_files, output_file):
    """合并多个pdf文件

    :param pdf_files: list
        需要合并的pdf文件列表
    :param output_file: str
        合并后的pdf文件路径
    """
    merger = PyPDF2.PdfFileMerger()
    for file in pdf_files:
        f = open(file, 'rb')
        file_rd = PyPDF2.PdfFileReader(f)
        # use file name as bookmark
        bookmark = os.path.basename(os.path.splitext(file)[0])
        if file_rd.isEncrypted:
            print('%s is encrypted, not supported!' % file)
            continue
        merger.append(file_rd, bookmark=bookmark, import_bookmarks=True)
        f.close()
    merger.write(output_file)
    merger.close()

