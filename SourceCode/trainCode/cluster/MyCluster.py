import  numpy as np

import  matplotlib.pyplot as plt

from sklearn.cluster import  AgglomerativeClustering
from sklearn.cluster import  KMeans

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat


def loadDataMat(fileName):
    X = []
    f = open(fileName)

    for v in f:
        X.append([float(v.split('\t')[0]), float(v.split('\t')[1])])
    X = np.array(X)
    return  X


def k_cluster():
    dataMat = loadDataMat('testSet2.txt')

    n_clusters = 4

    cls = KMeans(n_clusters)

    cls.fit(dataMat)

    cls.labels_

    makers = ['*', '^', '+', 'o']

    for i in range(n_clusters):
        members = cls.labels_ == i
        plt.scatter(dataMat[members, 0], dataMat[members, 1], s = 60, marker = makers[i], c = 'b', alpha = 0.5)

    plt.title('')
    plt.show()



if __name__ == '__main__':

    k_cluster()



