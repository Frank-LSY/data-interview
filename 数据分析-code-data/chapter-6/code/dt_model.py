import pandas as pd
from random import shuffle

#导入数据
datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

# 分割训练集/测试集
p = 0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

# 决策树
from sklearn.tree import DecisionTreeClassifier
treefile = '../tmp/tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])
from sklearn.externals import joblib
joblib.dump(tree,treefile)

# 混淆矩阵
from cm_plot import *
cm_plot(train[:,3],tree.predict(train[:,:3])).savefig('../tmp/dt_cm.png')

# ROC曲线
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
plt.clf()
fpr,tpr,thresholds = roc_curve(test[:,3],tree.predict_proba(test[:,:3])[:,1],pos_label=1)
plt.plot(fpr,tpr,linewidth=2,label='ROC of CART')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0,1.05)
plt.xlim(0,1.05)
plt.legend(loc=4)
plt.savefig('../tmp/dt_roc.png')

