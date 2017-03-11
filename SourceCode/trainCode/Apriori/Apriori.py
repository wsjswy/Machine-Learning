__author__ = 'wsjswy'


from  numpy import  *

def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()

    for i in C1:
        print(i)
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = len(D)
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

if __name__ == "__main__":

    dataset = loadDataSet()

    C1 = createC1(dataset);

    D = map(set, dataset)

    for i in D:
        print(i)

    L1, supprotData = scanD(D, C1, 0.5)

    prin(supprotData)