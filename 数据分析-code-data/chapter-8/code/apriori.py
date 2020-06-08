import pandas as pd

def connect_string(x,ms):
    x = list(map(lambda i:sorted(i.split(ms)),x))
    r = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i][:-1]==x[j][:-1] and x[i][-1]!=x[j][-1]:
                r.append(x[i][:-1]+sorted([x[i][-1],x[j][-1]]))
    return r

def find_rule(d,support,confidence,ms=u'---'):
    result = pd.DataFrame(index=['support','confidence'])

    support_series= 1.0*d.sum()/len(d)

    column = list(support_series[support_series>support].index)
    k = 0

    while len(column) >1:
        k = k+1
        print(u"\n正在进行第%s次搜索..." % k)

        column = connect_string(column,ms)
        print(u"数目%s..." % len(column))
        index_lst = [ms.join(i) for i in column]

        sf = lambda i:d[i].prod(axis=1,numeric_only=True)
        d_2 = pd.DataFrame(list(map(sf,column)),index=index_lst).T
        support_series_2 = 1.0*d_2.sum()/len(d)
        column = list(support_series_2[support_series_2>support].index)

        support_series = support_series.append(support_series_2)
        column_2 = []

        for i in column:
            i = i.split(ms)
            for j in range(len(i)):
                column_2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        confidence_series = pd.Series(index = [ms.join(i) for i in column_2])

        for i in column_2:
            confidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:-1])]

        for i in confidence_series[confidence_series>confidence].index:
            result[i] = 0.0
            result[i]['confidence'] = confidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort_values(['confidence','support'],ascending=False)
    print(u'\nresult:')
    print(result)

    return result