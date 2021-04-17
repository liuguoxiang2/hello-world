import pandas as pd
import re

# a = [a_ for a_ in newlist if a_ == a_] 去除nan得方法

def file_upload(path_file):
    newlist = []
    data = pd.read_excel(path_file)
    for row in data.values:
      for i in range(0,len(row)):
             newlist.append(row[i])
    b = [newlist[i:i + 6] for i in range(0, len(newlist), 6)]
    return b;

if __name__ == '__main__':
    data_dict = {}
    print(file_upload( 'G:\毕业论文\临床数据整理（预处理）-药名标准化(测试).xlsx'))
