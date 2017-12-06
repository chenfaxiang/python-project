#!/usr/bin/env python
# -*- coding: utf-8 -*-

' random generation 验证码 '
__author__ = 'ChenFaxiang'

import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

# Image       负责处理图片
# ImageDraw   负责处理画笔
# ImageFont   负责处理字体
# ImageFilter 负责处理滤镜

# 项目步骤
# 1. 定义一张图片
img = Image.new('RGB', (120, 50), (255, 255, 255))
                # 参数一 rgb颜色模式
                # 参数二 绘制的图片大小
                # 参数三 具体的图片颜色
# 2. 创建画笔
draw = ImageDraw.Draw(img)
# 3. 绘制线条和点
    # 绘制线
for i in range(random.randint(1, 10)):
    # 绘制线条时，每条线两个点，靠x,y来确定位置
    draw.line(
        [
            (random.randint(1, 120), random.randint(1, 120)),
            (random.randint(1, 120), random.randint(1, 120))
        ],
        fill = (0, 0, 0)
    )
    # 绘制点
for i in range(1000):
    draw.point(
        [
            (random.randint(1, 120), random.randint(1, 120)),
            (random.randint(1, 120), random.randint(1, 120))
        ],
        fill = (0, 0, 0)
    )
# 4. 绘制我们的文字
    # 文字随机产生的
    # 文字的个数是一定的
        # 定义要生成随机数的字母和数字
font_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
c_chars = ''.join(random.sample(font_list, 5))
    # random.sample是在指定的列表中随机取出指定个元素
    # 绘制字体
        # 先定制一下字体
font = ImageFont.truetype('KohinoorBangla.ttc', 32)
draw.text((6, 2), c_chars, font=font, fill='green')
    # 参数一 文字的位置，上、左
    # 参数二 文字内容
    # 参数三 字体
    # 参数四 字体颜色
# 5. 定义扭曲参数
parmas = [
    1 - float(random.randint(1, 2))/100,
    0,
    0,
    0,
    1 - float(random.randint(1, 2))/100,
    float(random.randint(1, 2))/500,
    0.001,
    float(random.randint(1, 1))/500
]
# 6. 使用滤镜
    # 添加滤镜
img = img.transform((120, 50), Image.PERSPECTIVE, parmas)
    # 参数一 扭曲范围
    # 参数二 扭曲样式
    # 参数三 扭曲参数

    # 进行扭曲
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

img.show()
