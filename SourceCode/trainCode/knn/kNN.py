__author__ = 'wsjswy'

from numpy import  *

import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]



    diffMat = tile(inX, [dataSetSize, 1])

    diffMat =  diffMat - dataSet


    print(diffMat)

    sqDiffMat = diffMat ** 2

    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5

    #获取距离

    sortedDistIndicies = distances.argsort()

    print(sortedDistIndicies)

    classCount = {}

    for i in range(k):
        votelabel1 = labels[sortedDistIndicies[i]]
        classCount[votelabel1] = classCount.get(votelabel1, 0) + 1

    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)

    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

#当处理不同范围的特征值的时候，通常采用的方法是数值归一化；
#将数值范围处理为0到1或者-1到1之间
#处理公式 newValue = (oldValue - minValue) / (maxValue - minValue)

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)

    ranges = maxVals - minVals
    normaDataSet = zeros(shape(dataSet))

    m = dataSet.shape[0]
    normaDataSet = dataSet - tile(minVals, (m, 1))
    normaDataSet =  normaDataSet / tile(ranges, (m, 1))
    return normaDataSet, ranges, minVals




def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print(errorCount)
if __name__ == "__main__":


    group, labels = createDataSet()

  #  print(group)

  #  print(classify0([0, 0], group, labels, 3))
  #
  #   dataSetFilePath = "datingTestSet2.txt"
  #
  #   datingDataMat, datingLabels = file2matrix(dataSetFilePath)
  #
  #   print(datingDataMat)
  #
  #
  #   print(len(datingLabels))
  #
  #   print(datingLabels[0:100])
  #
  #   fig = plt.figure()
  #   ax = fig.add_subplot(111)
  #   ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
  #   plt.show()

    datingClassTest()

