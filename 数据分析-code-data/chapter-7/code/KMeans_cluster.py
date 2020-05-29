import pandas as pd
from sklearn.cluster import KMeans

inputfile = '../tmp/zscoreddata.xls'
k = 5

data = pd.read_excel(inputfile)

kmodel = KMeans(n_clusters=k,n_jobs=2)
kmodel.fit(data)

kmodel.cluster_centers_ # 查看聚类中心
kmodel.labels_ # 查看各样本对应类别