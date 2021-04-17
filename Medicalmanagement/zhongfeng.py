import re
from collections import Counter


import xlwt
import xlrd
# import matplotlib.pyplot as plt
newlist = []


def extract(inpath):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表nj
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result = str(alldata[22])  # 取出表中药材的数据
        if(result!=''):
             newlist.append(result.split("、"))
    items = []
    for item in newlist:
        for j in item:
            res1 = ''.join(re.findall('[\u4e00-\u9fa5]', j))
            res2 = re.sub('\([\u4e00-\u9fa5]+\d+\)', '', res1) #去掉数字的
            items.append(res2)
        c = Counter(items)
    k = c.most_common(15)  # 找出全部元素前15的
    print(k)
    return k


inpath = 'F:\网络学习资料\临床数据整理（预处理）-药名标准化(1).xlsx'  # excel文件所在路径
extract(inpath)





# x = list(dict(k).keys()) # 取院系的那一列
# y = list(dict(k).values()) # 取数字的那一列
#
# x1 = list(dict(a1).keys()) # 取院系的那一列
# y1 = list(dict(a1).values()) # 取数字的那一列
#
# wbk = xlwt.Workbook() #定义一个workbook对象
# sheet = wbk.add_sheet("wordCount")#新建一个sheet并命名
# for i in range(len(x1)):
#     sheet.write(i, 1, label = y1[i])
#     sheet.write(i, 0, label = x1[i])
# wbk.save(r'G:\毕业论文\中风药物分析.xlsx')
#
#
#
# plt.bar(x, y, align='center')  # 画图，设置x，y轴的数据
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# for x, y in zip(x, y):
#      plt.text(x, y + 0.4, '%.0f' % y, ha='center', va='bottom')
# plt.show()










