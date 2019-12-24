# -*- coding: utf-8 -*-
import math
import re

import pandas as pd
import requests
import xlwt
from bs4 import BeautifulSoup
from tqdm import tqdm


class lianjia():
    def __init__(self):
        print('*******lianjia_spider******')
        print('Author : okc')
        print('Date : 2019-12-19')
        print('Version: Python3.8')
        print('**************************\n')

        self.pattern = re.compile(
            '<div class="info clear">.*?target="_blank">(.*?)</a>.*?class="houseInfo"><span class="houseIcon"></span>(.*?)</div></div>.*?class="totalPrice"><span>(.*?)</span>万.*?class="unitPrice".*?<span>(.*?)</span></div></div></div>')
        self.house_num_pattern = re.compile('共找到<span> (.*?) </span>套(.*?)二手房')
        self.area_dic = {'雨花': 'yuhua',
                         '岳麓': 'yuelu',
                         '天心': 'tianxin',
                         '开福': 'kaifu',
                         '芙蓉': 'furong',
                         '望城': 'wangcheng',
                         '宁乡': 'ningxiang',
                         '浏阳': 'liuyang',
                         '长沙县': 'changshaxian'
                         }

    def get_info(self, url):
        html = requests.get(url).text
        html = html.encode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        infos = soup.find_all(class_="info clear")
        return infos

    def get_content(self, info, area):
        info_dic = {}
        info = re.findall(self.pattern, str(info))
        # info = self.getHouseInfo(self, info)
        if info:
            info = list(info[0])
            info_dic['title'] = info[0].strip()
            info_dic['totalPrice'] = info[2].strip() + '万'
            info_dic['unitPrice'] = info[3].strip()
            house_list = info[1].split('|')

            # 封装数据
            info_dic['huxing'] = house_list[0].strip()
            info_dic['size'] = house_list[1].strip()
            info_dic['orientations'] = house_list[2].strip()
            info_dic['house_style'] = house_list[3].strip()
            info_dic['floor'] = house_list[4].strip()

            # 有些数据多了房子的修建时间
            if len(house_list) == 6:
                info_dic['apartment_layout'] = house_list[5].strip()
            else:
                info_dic['built_time'] = house_list[5].strip()
                info_dic['apartment_layout'] = house_list[6].strip()
                return info_dic
        else:
            return {}

    def getHouseInfo(self, info):
        houseInfo = re.findall(self.pattern, str(info))
        if houseInfo:
            return houseInfo
        else:
            print(str(info))
            return ""

    def run(self):
        data = pd.DataFrame()
        # 创建一个Excel 工作空间
        workbook = xlwt.Workbook(encoding='utf-8')
        for area in self.area_dic.keys():
            print('>>>> 正在保存%s的二手房信息>>>\n' % area)
            url = 'https://cs.lianjia.com/ershoufang/%s/' % self.area_dic[area]
            r = requests.get(url).text
            self.house_num_pattern = re.compile('共找到<span> (.*?) </span>套%s二手房' % area)
            house_num = re.findall(self.house_num_pattern, r)[0].strip()
            total_page = int(math.ceil(int(house_num) / 30.0))
            if total_page >= 100:
                total_page = 100
            else:
                pass

            # 创建sheet 页
            sheet = workbook.add_sheet(area)
            # 创建表头数据
            head = ['标题', '总价', '单价', '户型', '大小', '朝向', '装修程度', '楼层位置', '修建时间', '楼房结构']
            for h in range(len(head)):
                sheet.write(0, h, head[h])
            i = 1
            for page in tqdm(range(total_page)):
                url = 'https://cs.lianjia.com/ershoufang/%s/pg%s/' % (self.area_dic[area], str(page + 1))
                infos = self.get_info(url)
                for info in infos:
                    info_dic = self.get_content(info, area)
                    if info_dic:
                        sheet.write(i, 0, info_dic['title'])
                        sheet.write(i, 1, info_dic['totalPrice'])
                        sheet.write(i, 2, info_dic['unitPrice'])
                        sheet.write(i, 3, info_dic['huxing'])
                        sheet.write(i, 4, info_dic['size'])
                        sheet.write(i, 5, info_dic['orientations'])
                        sheet.write(i, 6, info_dic['house_style'])
                        sheet.write(i, 7, info_dic['floor'])
                        sheet.write(i, 8, info_dic['built_time'])
                        sheet.write(i, 9, info_dic['apartment_layout'])
                        i+=1
                        print('>>>> 链家二手房数据已保存❗----------%s' % area)

        workbook.save('changsha.xlsx')


if __name__ == '__main__':
    x = lianjia()
    x.run()
