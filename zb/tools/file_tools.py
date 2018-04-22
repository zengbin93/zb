# -*- coding: utf-8 -*-
import os
import shutil
import zipfile


def legitimize(text):
    """Converts a string to a valid filename.
    """
    import platform
    os = platform.system()
    # POSIX systems
    text = text.translate({
        0: None,
        ord('/'): '-',
        ord('|'): '-',
    })

    if os == 'Windows':
        # Windows (non-POSIX namespace)
        text = text.translate({
            # Reserved in Windows VFAT and NTFS
            ord(':'): '-',
            ord('*'): '-',
            ord('?'): '-',
            ord('\\'): '-',
            ord('\"'): '\'',
            # Reserved in Windows VFAT
            ord('+'): '-',
            ord('<'): '-',
            ord('>'): '-',
            ord('['): '(',
            ord(']'): ')',
        })
    else:
        # *nix
        if os == 'Darwin':
            # Mac OS HFS+
            text = text.translate({
                ord(':'): '-',
            })

        # Remove leading .
        if text.startswith("."):
            text = text[1:]

    text = text[:82]  # Trim to 82 Unicode characters long
    return text


def modify_content(file, old, new):
    """替换文件中的指定内容"""
    try:
        lines = open(file, 'r').readlines()
        f_len = len(lines) - 1
        for i in range(f_len):
            if old in lines[i]:
                lines[i] = lines[i].replace(old, new)
        open(file, 'w').writelines(lines)
    except Exception as e:
        print(e)


def batch_del_file(path, in_name=None, yn=None):
    """批量删除文件（给出一定的规则）"""
    if in_name is None:
        file_to_del = [os.path.join(path, i) for i in os.listdir(path)]
    else:
        file_to_del = [os.path.join(path, i) for i in os.listdir(path) if in_name in i]
    print('以下是要删除的文件列表：\n')
    print(file_to_del)

    if yn is None:
        yn = input('删除以上文件（输入：y/n）, 保留部分文件（输入：k）：')

    if yn == 'k':
        file_to_save = []
        while True:
            f = input('请输入要保留的文件名（输入“b”结束）：')
            if f == 'b':
                break
            file_to_save.append(f)
        file_to_del = [i for i in file_to_del if i not in file_to_save]
        for file in file_to_del:
            os.remove(file)
            print('已删除：', file)
    elif yn == 'y' or yn == 'yes':
        for file in file_to_del:
            os.remove(file)
            print('已删除：', file)
    else:
        print('文件没有删除')


def batch_move_file(path, dest, in_name=None):
    """将path目录下文件名中包含的in_name的文件移动到dest目录下

    parameters
    ------------
    path        需要转移文件的目录
    dest        目标目录
    in_name     str, 默认是None。文件名过滤规则

    example
    ------------
    # 将path目录下的所有txt文件转移到dest目录
    move_file(path, dest, in_name='.txt')
    """
    assert os.path.exists(path), '%s 文件夹不存在' % path
    assert os.path.exists(dest), '%s 文件夹不存在' % dest
    if in_name is None:
        file_list = os.listdir(path)
    else:
        file_list = [i for i in os.listdir(path) if in_name in i]
    if len(file_list) != 0:
        for file in file_list:
            f = os.path.join(path, file)
            d = os.path.join(dest, file)
            shutil.move(f, d)
            print('已转移：%s' % f)
    else:
        if in_name is None:
            print('%s 中没有文件' % path)
        else:
            print('%s 中没有包含【 %s 】的文件' % (path, in_name))


# TODO(ZB):创建一个批量复制指定文件（支持正则匹配）的函数
def make_zip(folder_path, output_filename):
    """将目录中除zip之外的文件打包成zip文件(包括子文件夹)
    空文件夹不会被打包

    example
    ----------------
    make_zip('results','zips//招标信息结果_2017-05-09.zip')
    """
    cwd = os.getcwd()
    # 获取需要打包的文件列表
    file_lists = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_1 = os.path.join(root, file).replace(folder_path + '/', '')
            if 'zip' not in file_1:
                file_lists.append(file_1)
    # 将文件列表打包成zip
    os.chdir(folder_path)
    with zipfile.ZipFile(output_filename, 'w') as myzip:
        for file in file_lists:
            myzip.write(file)
    # 将工作目录切换回原始
    os.chdir(cwd)


def create_file(file, content=None, mode="a", encoding='utf-8'):
    with open(file, mode, encoding=encoding) as f:
        if isinstance(content, str):
            content += "\n"
            f.write(content)
        elif isinstance(content, list):
            content = [i.strip("\n")+'\n' for i in content]
            f.writelines(content)
        elif content is None:
            return
        else:
            raise ValueError("If content is not None, it must be list or str!")


def write_file(file, content, mode='a', encoding='utf-8'):
    create_file(file, content=content, mode=mode, encoding=encoding)


def read_file(file, encoding='utf-8'):
    with open(file, 'r', encoding=encoding) as f:
        lines = f.readlines()
        lines = [line.strip("\n") for line in lines]
    if len(lines) > 0:
        return lines
    else:
        raise ValueError("file is empty!")



