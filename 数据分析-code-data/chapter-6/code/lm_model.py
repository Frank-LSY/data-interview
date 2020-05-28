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

#LM神经网络
from keras.models import Sequential
from keras.layers.core import Dense,Activation

netfile = '../tmp/net.model'
# 构建神经网络
net = Sequential()
net.add(Dense(10,input_shape=(3,)))
net.add(Activation('relu'))
net.add(Dense(1,input_shape=(10,)))
net.add(Activation('sigmoid'))
net.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_accuracy'])
# 喂数据、训练、预测
net.fit(train[:,:3],train[:,3],epochs=100,batch_size=1)
net.save_weights(netfile)
predict_result = net.predict_classes(train[:,:3]).reshape(len(train))
# 混淆矩阵图
from cm_plot import *
cm_plot(train[:,3],predict_result).savefig('../tmp/lm_cm.png')

# ROC曲线
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
plt.clf()
predict_result = net.predict(test[:,:3]).reshape(len(test))
fpr,tpr,thresholds = roc_curve(test[:,3],predict_result,pos_label=1)
plt.plot(fpr,tpr,linewidth=2,label='ROC of LM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0,1.05)
plt.xlim(0,1.05)
plt.legend(loc=4)
plt.savefig('../tmp/lm_roc.png')