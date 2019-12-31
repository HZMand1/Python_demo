import os

import pandas as pd


class read_excel_list():
    def __init__(self):
        print('*******lianjia_spider******')
        print('Author : okc')
        print('Date : 2019-12-19')
        print('Version: Python3.8')
        print('**************************\n')

        self.dir = "D:\\test"

    def get_file_list(self):
        file_list = []
        if os.path.isdir(self.dir):
            for file in os.listdir(self.dir):
                file_path = os.path.join(self.dir, file)  # 获取绝对路径
                if os.path.splitext(file_path)[1] == '.xls' or os.path.splitext(file_path)[
                    1] == '.xlsx':  # 判断文件是否是Excel文件
                    file_list.append(file_path)
            return file_list  # 返回Excel文件路径列表
        return []

    def run(self):
        print("Start run function")

        file_list = self.get_file_list()
        for file in file_list:
            print(file)
            # # 1：读取指定行
            # 这个会直接默认读取到这个Excel的第一个表单
            df = pd.read_excel(file)
            test_data = []
            for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
                # 根据i来获取每一行指定的数据 并利用to_dict转成字典
                row_data = df.ix[
                    i, ['修建时间', '单价', '大小', '总价', '户型', '标题', '朝向', '标题', '楼层位置', '楼房结构']
                ].to_dict()
                test_data.append(row_data)
            print("最终获取到的数据是：{0}".format(test_data))

        # file_list = self.get_file_list(self)
        # print(file_list)
        # # 1：读取指定行
        # df = pd.read_excel('lemon.xlsx')  # 这个会直接默认读取到这个Excel的第一个表单
        # data = df.ix[0].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
        # print("读取指定行的数据：\n{0}".format(data))


if __name__ == '__main__':
    read_excel_list().run()
