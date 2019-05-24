# -*- coding: utf-8 -*-
from PIL import Image
import os, sys

save_image_name = "./New.png"
raw_name = "./raw.bmp"
res_file = "../images"  # 资源照片路径
mw = 300  # 单个照片的尺寸


def load_raw(raw_name, data_list, _size):
    im = Image.open(raw_name)
    w, h = im.size

    for i in range(w):
        for j in range(h):
            v = im.getpixel((i, j))
            if v != 0:
                # 将灰度图的像素映射到照片墙的坐标内
                x = int(i * _size[0] / w)
                y = int(j * _size[1] / h)
                data_list[x][y] = 1


def get_picture_list(picture_list):
    for filename in os.listdir(res_file):
        filepath = os.path.join(res_file, filename)
        picture_list.append(filepath)


# 绘制一张照片到指定位置
def draw_picture(save_image, x, y, im_name):
    in_image = Image.open(im_name)
    in_image = in_image.resize((mw, mw), Image.ANTIALIAS)
    # save_image.paste(in_image, ((x - 1) * mw, (y - 1) * mw))
    save_image.paste(in_image, (x * mw, y * mw))

def main():
    # 照片墙能容纳的最大照片数量 3 * 3
    w, h = (5, 5)
    data_list = [[0 for col in range(h)] for row in range(w)]

    # 加载灰度图, 照片墙样式
    load_raw(raw_name, data_list, (w, h))
    # 创建一张新的照片
    save_image = Image.new('RGBA', (mw * w, mw * h))

    # 获取所有照片路径名称
    picture_list = []
    get_picture_list(picture_list)

    pos = 0
    print(picture_list)
    # 按照样式, 缩放绘制照片到指定位置
    for i in range(w):
        for j in range(h):
            if data_list[i][j] > 0:
                draw_picture(save_image, i, j, picture_list[pos])
                print(i, j)
                pos += 1
                pos = pos % len(picture_list)

    # 保存
    save_image.show()
    save_image.save(save_image_name)


if __name__ == '__main__':
    main()