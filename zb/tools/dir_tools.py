# -*- coding: utf-8 -*-
import os
import shutil


def clean_folder(folder):
    """清空文件夹，并确保文件夹存在"""
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

def insure_folder_exists(folder):
    """确保文件夹存在"""
    if not os.path.exists(folder):
        os.mkdir(folder)

# def get_file_list(folder_path, form='view', graph=True):
def get_file_list(folder_path):
    """将folder_path文件夹下的所有文件的相对路径保存到txt文件中

    params
    ---------
    folder_path     文件夹路径
    form            文件名保存形式，可选 'view' 'full'
    """
    import os
    f = open(folder_path + '\\file_list.txt', 'w')
    # f.write('根目录：\n')
    # 写入文件相对路径
    for root, dirs, files in os.walk(folder_path):
        x = ''
        for file in files:
            if root != x:  # 如果不是同一个root，换行
                f.write('\n' + root.replace(folder_path+'\\', '') + '\n')
            file_1 = os.path.join(root, file)
            file_2 = file_1.replace(root+'\\', '')
            f.write('  |-- ' + file_2 + '\n')
            x = root
    f.close()



