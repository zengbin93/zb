# -*- coding: utf-8 -*-
"""
Create Date: 2017-07-24
python代码分析工具
输入：
    单个（多个）脚本路径  or   项目路径

输出：
    分析结果（md文件）

功能：
    1、统计单个脚本中定义的函数、类的数量，并将函数名和类名分别保存
    2、

"""

import os

py_path = r'C:\Anaconda3\Lib\zb_CodeSet\local_use'
fn_pys = [os.path.join(py_path, fn) for fn in os.listdir(py_path)]

def read_py(fn_py):
    """将py文件读入"""
    with open(fn_py, 'r', encoding='utf-8') as pyf:
        lines = pyf.readlines()
    return lines

def save_py(save_lines, fn_py):
    """保存处理之后的代码"""
    with open(fn_py, 'w', encoding='utf-8') as pyf:
        pyf.writelines(save_lines)

def del_annotation(py_lines):
    """删除以#开头的单行注释"""
    save_lines = []
    for i in range(1, len(py_lines)):
        if not py_lines[i].strip(' ').startswith('#'):
            save_lines.append(py_lines[i])
    return save_lines

# fn_py = fn_pys[1]
# py_lines = read_py(fn_py)
# save_lines = del_annotation(py_lines)
# save_py(save_lines, fn_py)
