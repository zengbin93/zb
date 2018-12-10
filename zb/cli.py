# -*- coding: utf-8 -*-

import click
import time


@click.group()
def zb():
    pass


@zb.command()
@click.option('-p', '--path', help="文件路径")
@click.option('-f', '--f', help="文件名中需要修改的内容")
@click.option('-t', '--t', help="修改之后的内容")
def brf(path, f, t):
    """batch_rename_file | 批量重命名文件"""
    from .tools.file import batch_rename_file
    batch_rename_file(path, f, t)


@zb.command()
def ts():
    """timestamp | 查看当前时间戳"""
    print("当前时间戳：", time.time())


@zb.command()
def km():
    """keyboard monitor | 键盘记录器"""
    from zb.dev.keyboard import run_keyboard_monitor
    run_keyboard_monitor()


if __name__ == "__main__":
    zb()
