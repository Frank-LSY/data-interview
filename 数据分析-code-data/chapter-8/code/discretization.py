from __future__ import print_function
import pandas as pd
from sklearn.cluster import KMeans

datafile = '../data/data.xls'
processedfile = '../tmp/data_processed.xls'
typelabel = {u'肝气郁结证型系数':'A',u'热毒蕴结证型系数':'B',
             u'冲任失调证型系数':'C',u'气血两虚证型系数':'D',
             u'脾胃虚弱证型系数':'E',u'肝肾阴虚证型系数':'F'}
k = 4

data = pd.read_excel(datafile)
keys = list(typelabel.keys())
result = pd.DataFrame()

if __name__ == '__main__':
    for i in range(len(keys)):
        print(u'正在进行"%s"的聚类...' %keys[i])
        kmodel = KMeans(n_clusters=k,n_jobs=2)
        kmodel.fit(data[[keys[i]]].as_matrix())

        r1 = pd.DataFrame(kmodel.cluster_centers_,columns=[typelabel[keys[i]]])
        # 聚类中心
        r2 = pd.Series(kmodel.labels_).value_counts()

        # 分类统计
        r2 = pd.DataFrame(r2,columns=[typelabel[keys[i]]+'n'])
        r = pd.concat([r1,r2],axis=1).sort_values(typelabel[keys[i]])

        r.index = [1,2,3,4]
        r[typelabel[keys[i]]] = pd.Series.rolling(r[typelabel[keys[i]]],2).mean()
        r[typelabel[keys[i]]][1] = 0.0
        print(r.T)
        result = result.append(r.T)

    result = result.sort_index()
    print(result)
    result.to_excel(processedfile)