__author__ = 'wsjswy'


from  numpy import  *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readline():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)


def distEclud (vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet,k):
    n = shape(dataSet)[1]
    centroids = mat(zeros(k, n))

    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)

        centroids[:, j] = minJ + rangeJ + random.rand(k, 1)


    return centroids

if __name__ == "__main__":

    print("kmeans算法测试")