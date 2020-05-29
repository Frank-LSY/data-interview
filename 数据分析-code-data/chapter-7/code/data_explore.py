import pandas as pd

datafile = '../data/air_data.csv'
resultfile = '../tmp/explore.xls'

data = pd.read_csv(datafile,encoding='utf-8')

explore = data.describe(percentiles=[],include='all').T # percentile为分位数，此处不需计算，转置可得到表头
# print(explore)
explore['null'] = len(data)-explore['count']

explore = explore[['null','max','min']]
explore.columns = [u'空值数',u'最大值',u'最小值']
explore.to_excel(resultfile)
