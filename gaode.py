#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a *.py module '
__author__ = 'ChenFaxiang'

from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
# import html5lib

# 爬取的目标地址
URL = 'http://bj.ganji.com/fang1/xisanqi/m1p7/'
ADDR = 'http://bj.ganji.com/'


if __name__ == '__main__':
    start_page = 1 # 从第一页开始
    end_page = 10  # 在第十页结束
    price = 7000   # 价格
    with open('ganji.csv', 'wb') as f: # 创建一个csv文件
        # f = open('ganji.csv', 'wb')  wb是设置权限

        # '天通苑一区', '天通苑', '7000'
        csv_writer = csv.writer(f, delimiter = ',')

        print('start.........')

        while start_page <= end_page:
            start_page += 1
            print('get:{0}'.format(URL.format(page = start_page, price = price)))

            response = requests.get(URL.format(page = start_page, price = price))

            # 创建一个html对象，第一个参数是要抓取的对象，第二个参数是使用哪种解释器(python默认解析器)
            html = BeautifulSoup(response.text, 'html.parser')
            # 页面上房源信息的dom上class信息
            house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap')
            if not house_list:
                break

            for house in house_list:
                house_title = house.select('.title > a')[0].text.encode('utf-8')
                house_addr = house.select('.address > .area > a')[-1].string.encode('utf-8')
                house_price = house.select('.info > .price > .num')[0].string.encode('utf-8')
                house_url = urljoin(ADDR, house.select('.title > a')[0]['href'])
                csv_writer.writerow([house_title, house_addr, house_price, house_url])

        print('end............')

