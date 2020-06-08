import pandas as pd


datafile = '../data/data.xls'
apriorifile = '../data/apriori.txt'
all_out = '../tmp/all_apriori.txt'


data = pd.read_excel(datafile)
apriori = pd.read_csv(apriorifile,header=None,names=['A','B','C','D','E','F','H'])

data.rename(columns = {u'病程阶段':'S',u'转移部位':'R',
                       u'确诊后几年发现转移':'J'},inplace=True)
# apriori.rename(columns={'0':'A','1':'B','2':'C',
#                         '3':'D','4':'E','5':'F'},inplace=True)

print(apriori)
s = data['S']
r = data['R']
j = data['J']

s = pd.concat([apriori,s],axis=1)
sr = pd.concat([s,r],axis=1)
srj = pd.concat([sr,j],axis=1)

print(srj)
# srj.set_index(['A','B','C','D','E','F','H','S','R','J'])
srj.to_csv(all_out,index=False)