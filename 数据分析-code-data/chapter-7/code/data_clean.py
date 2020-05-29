import pandas as pd

datafile = '../data/air_data.csv' # 原始数据，第一行为属性标签
cleanedfile = '../tmp/data_cleaned.xls' # 输出数据

data = pd.read_csv(datafile,encoding='utf-8') # 读入数据

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()] # 票价需为非空值

index1 = data['SUM_YR_1'] != 0 # 第一年票价不为0
index2 = data['SUM_YR_2'] != 0 # 第二年票价不为0
index3 = (data['SEG_KM_SUM']==0) & (data['avg_discount']==0) # 总里程为0且折扣为0

data = data[index1|index2|index3] # 三者满足其一

data.to_excel(cleanedfile)