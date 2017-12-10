#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 图片转换字符画 '
__author__ = 'ChenFaxiang'

from PIL import Image
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('file') # 输入文件
parse.add_argument('-0', '--output') # 输出文件
parse.add_argument('--width', type = int, default = 100) # 输出字符画宽度
parse.add_argument('--height', type = int, default = 30) # 输出字符画高度

# 获取参数
args = parse.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 指定灰度值
# 用灰度值公式将像素的RGB值映射到灰度值
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length

    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    # resize 改变图像的大小
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
            # getpixel 是获取某个像素位置的值
        txt += '\n'

    print txt

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
