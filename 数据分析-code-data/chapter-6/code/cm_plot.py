from sklearn.metrics import confusion_matrix, roc_curve
import matplotlib.pyplot as plt

def cm_plot(y, yp):
    cm = confusion_matrix(y, yp)
    plt.matshow(cm, cmap=plt.cm.PuBu)
    plt.colorbar()

    for x in range(len(cm)):
        for y in range(len(cm)):
            plt.annotate(
                cm[x, y],
                xy=(x, y),
                horizontalalignment='center',
                verticalalignment='center')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return plt