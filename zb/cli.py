# -*- coding: utf-8 -*-

import click


@click.group()
def zb():
    pass

@zb.command()
@click.option('-p', '--path', help="文件路径")
@click.option('-f', '--f', help="文件名中需要修改的内容")
@click.option('-t', '--t', help="修改之后的内容")
def brf(path, f, t):
    """batch_rename_file | 批量重命名文件"""
    from .tools.file_tools import batch_rename_file
    batch_rename_file(path, f, t)

if __name__ == "__main__":
    zb()

