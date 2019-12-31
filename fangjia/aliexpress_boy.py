import bs4
import requests
import re
import xlwt
import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d')  # 给文件打上时间戳，便于数据更新
print(date)
# 网址 https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20191225081741&SearchText=Baby+Toys
url = 'https://www.aliexpress.com/wholesale'  # 网址
# 'initiative_id': 'SB_20191225081741', 这个参数好像没用到
payload = {'catId': '0', 'SearchText': 'Baby+Toys'}  # 字典传递url参数


# 初始化数据容器
title = []
price = []
order = []
store = []

resp = requests.get(url, params=payload)
soup = bs4.BeautifulSoup(resp.text, "html.parser")
print(resp.text)
print(resp.url)  # 打印访问的网址
resp.encoding = 'utf-8'  # 设置编码
all_ul_items = soup.find_all('div', class_=re.compile("right-menu"))
print(len(all_ul_items))
for j in all_ul_items:
    soup_title = bs4.BeautifulSoup(str(j), "html.parser", )
    print(soup_title.a['title'])

data=open("D:\\data.txt", 'w+')
print('这是个测试', file=data)
data.close()
