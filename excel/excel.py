#!usr/bin/env python
#coding: utf-8

import xlsxwriter

# 1.创建一个excel文件
work = xlsxwriter.Workbook("test.xlsx")

# 5.创建图表
chart = work.add_chart({type: 'column'})
    # 不可以插入空的图表

# 2.创建一个表格
worksheet = work.add_worksheet('表格名')
    # column 柱状图
    # area 面积图
    # bar 条形图
    # line 折线图
    # radar 雷达图

# 6.添加图标数据
    # 声明一个数据的容器
title = 'abcdef'
data = [1, 22, 32, 15, 18, 51]
for index, name in enumerate(title):
    point = 'A:%d'%(index + 1)
    worksheet.write(point, name)

for i, j in enumerate(data):
    point = 'B:%d'%i + 1
    worksheet.write(point, j)

# 7.为图标添加数据
chart.add_series({
    'categorys': '=表格名!$a$1:$a$9', # 类别标签范围
    'values': '=表格名!$b$1:$b$9',    # 图标数据范围
    'line': {'color': 'red'}       # 图标线条粗细
})
worksheet.insert_chart('A10', chart)


'''
# 3.修改内容格式
    # 表格格式
    # 内容的格式
worksheet.set_column('A:A', 20) # 设置单元格宽度
bold = work.add_format({'bold': True}) # 定义一个内容的样式

# 4.写入内容到表内 表内的单元格是两个坐标对应一个单元格
# A1 单元格是第一行第一列的第一个
    # 写入字符
worksheet.write('A1', '第一个单元格的内容', bold)
    # 写入图片
worksheet.insert_image('A2', '1.jpg')
    # 写入函数
worksheet.insert_image('A3', 2, bold)
worksheet.insert_image('A4', 20, bold)
worksheet.write('A5', '=SUM(A3:A4)', bold)
'''

# 关闭且保存excel
work.close()
