from __future__ import print_function
import pandas as pd
from apriori import *
import time

inputfile = '../tmp/all_apriori.txt'
data = pd.read_csv(inputfile,header=None,dtype=object)

start = time.clock()
print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x :pd.Series(1,index=x[pd.notnull(x)])
b = list(map(ct,data.as_matrix()))
data = pd.DataFrame(b).fillna(0)
end = time.clock()
print(u'\n转换完毕，用时：%0.2f秒' %(end-start))
del b

support = 0.06
confidence = 0.75
ms = '---'

start = time.clock()
print(u'\n开始搜索关联规则...')
find_rule(data,support,confidence,ms)
end = time.clock()
print(u'\n搜索完成，用时:%0.2f秒' %(end-start))