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
URL = 'https://i.youku.com/i/UNTY5MDQ5Njcy/videos?spm=a2hzp.8244740.0.0'


if __name__ == '__main__':
    start_page = 1 # 从第一页开始
    end_page = 1  # 在第end_page页结束

    with open('youku.csv', 'wb') as f: # 创建一个csv文件
        # f = open('youku.csv', 'wb')  wb是设置权限

        # 'youku', '视频播放量', '粉丝数'
        csv_writer = csv.writer(f, delimiter = ',')

        print('start.........')

        while start_page <= end_page:
            start_page += 1
            print('get:{0}'.format(URL.format(page = start_page)))

            response = requests.get(URL.format(page = start_page))

            # 创建一个html对象，第一个参数是要抓取的对象，第二个参数是使用哪种解释器(python默认解析器)
            html = BeautifulSoup(response.text, 'html.parser')
            # 页面上房源信息的dom上class信息
            video_list = html.select('.head-box > .head-info > .user-state')
            if not video_list:
                print('break............')
                break

            for curVideo in video_list:
                print('in............')
                video_play_num = curVideo.select('ul > .vnum')[0]['title']
                video_fans_num = curVideo.select('ul > .snum')[0]['title']

                csv_writer.writerow([video_play_num, video_fans_num])

        print('end............')
