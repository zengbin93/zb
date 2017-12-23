# -*- coding: utf-8 -*-
"""
python module fast migration
"""
import os

# step 1. get module installed list
def get_module_list(upgrade=False):
    requirements = r'c:\module_installed.txt'
    os.system('pip list >> ' + requirements)

    # read file, modify format
    with open(requirements, 'r') as f:
        lines = f.readlines()
        if not upgrade:
            modules = [i.replace(')', '').replace('(', '== ') for i in lines]
        else:
            modules = [i.replace(')', '').replace('(', '>= ') for i in lines]

    # write results to file
    with open(requirements, 'w') as f:
        f.writelines(modules)

# step 2. install modules in another machine
def install_module_list():
    requirements = r'c:\module_installed.txt'
    os.system('pip install -r ' + requirements)

def install_module_list_without_stop():
    requirements = r'c:\module_installed.txt'
    with open(requirements, 'r') as f:
        module_list = f.readlines()
    for lib in module_list:
        try:
            os.system('pip install ' + lib.strip('\n'))
        except Exception:
            print('pip 安装模块 %s 出错' % lib.strip('\n'))
