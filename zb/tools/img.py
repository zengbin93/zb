# -*- coding: utf-8 -*-

from PIL import Image
import os


def img2pdf(path, pdf_name=None):
    """合并path目录下的所有图片到pdf文件中

    :param path: str
        图片路径
    :param pdf_name: str
        默认值 图片路径.pdf; pdf文件名
    """
    print("merge images in %s ..." % path)
    if not pdf_name:
        pdf_name = os.path.join(path, '%s.pdf' % os.path.split(path)[1])
    file_list = os.listdir(path)

    # filter pic in path
    pic_names = []
    img_suffix = ['.png', '.jpg', '.jpeg']
    for x in file_list:
        _, suffix = os.path.splitext(x)
        if suffix.lower() in img_suffix:
            pic_names.append(os.path.join(path, x))
    pic_names.sort()

    if len(pic_names) == 0:
        print("There is no images in %s" % path)
        return

    im_list = []
    im1 = Image.open(pic_names[0])
    pic_names.pop(0)
    for i in pic_names:
        img = Image.open(i)
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True,
             append_images=im_list)
    print("images saved to：", pdf_name)
