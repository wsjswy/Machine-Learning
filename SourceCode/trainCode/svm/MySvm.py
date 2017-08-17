from  sklearn  import svm
import  numpy as np
import  matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import  Axes3D

# X = [[0, 0], [1, 1]]
# y = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)
#
# s_result = clf.predict([0, -1])
# print(s_result)

def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

if __name__ == '__main__':
    print('---SVM  TEST----')

    clf = svm.SVC(decision_function_shape='ovo', kernel='rbf')

    X, Y = loadDataSet('testSetRBF.txt')

    # clf.fit(np.array(X), np.array(Y))
    clf.fit(X, Y)

    print(clf.fit(X, Y))

    print(clf.predict(np.array([0.000, 0.000]).reshape(1,-1)))

    print("支持向量信息： " + str(len(clf.support_vectors_)))

    print("支持向量系数： " + str(clf.support_))

    print(clf.n_support_)

    # #plt画图
    # plt.figure("svm") #创建图表
    #
    # for point in X:
    #     plt.scatter(point[0], point[1], color ='green')
    #
    #
    # for point2 in clf.support_vectors_:
    #     plt.scatter(point2[0], point2[1], color = 'red')
    #
    # # plt.plot(clf.n_support_, color = 'red')
    #
    # plt.show()

    dec = clf.decision_function(X[0])
    clf.decision_function_shape = 'ovr'
    dec = clf.decision_function(X[1])
    print(dec.shape[0])
