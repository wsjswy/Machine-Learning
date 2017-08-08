from  math import  log

import  operator


def clacEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannoEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannoEnt -= prob * log(prob, 2)

    return  shannoEnt


def crateDataSet():

    dataSet = [ [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']
    ]

    labels = ['no surfacing',  'flippers']

    return  dataSet, labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numberFeatures = len(dataSet[0]) - 1
    baseEntropy = clacEnt(dataSet)
    baseInfoGain = 0.0
    bestFeature = -1
    for i in range(numberFeatures):
        featurelist = [t[i] for t in dataSet]
        uniqueVals = set(featurelist)
        newEntroy = 0.0

        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob  = len(subDataSet) /float(len(dataSet))
            newEntroy += prob * clacEnt(subDataSet)

        infoGain = baseEntropy - newEntroy

        if (infoGain > baseInfoGain):
            baseInfoGain = infoGain
            bestFeature = i
    return  bestFeature



def majorityCnt(classList):
    classCount= {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1

    sortedClassCount = sorted(classCount.items(),  key = operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [t[-1] for t in dataSet]  #类别

    if classList.count(classList[0]) == len(classList):
        return  classList[0]

    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet) #获取最佳分类属性

    bestFeatLabel1 = labels[bestFeat]

    myTree = {bestFeatLabel1: {}}

    del(labels[bestFeat])

    featValues = [ t[bestFeat] for t in dataSet]
    uniqueVals = set(featValues)

    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel1][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return  myTree




if __name__ == "__main__":

    dataSet, labels =  crateDataSet()

    myTree = createTree(dataSet, labels)

    print(myTree)
