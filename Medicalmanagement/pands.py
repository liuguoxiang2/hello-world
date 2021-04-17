import pandas as pd
import re



def getCount_Dict(data_dict, path_file):

    newlist = []
    data = pd.read_excel(path_file)
    print(data_dict)
    for row in data.values:
        if (row[22] != ''):
            newlist.append(row[22])
    a = [a_ for a_ in newlist if a_ == a_]
    for row in a:
        for k in re.findall('[\u4e00-\u9fa5]{0,10}', row):
            if len(k) >= 0:
                data_dict[k] = data_dict.get(k, 0) + 1
    del(data_dict[''])

    return dict(sorted(data_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

if __name__ == '__main__':
    data_dict = {}
    print(getCount_Dict(data_dict, 'F:\网络学习资料\临床数据整理（预处理）-药名标准化(1).xlsx'))
