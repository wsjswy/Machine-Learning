from numpy import *
from time import sleep
import  json
import  urllib
import  matplotlib.pyplot as plt

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    datMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))

        datMat.append(lineArr)
        labelMat.append(float(curLine[-1]))


    return datMat, labelMat


# def panitRawData(xArr, yArr):
#     xMat = mat(xArr)
#     yMat = mat(yArr)
#     yMatT= yMat.T
#     flg = plt.figure()
#     ax = flg.add_subplot(111)
#     ax.scatter(xMat[:,1].flatten().A[0], yMatT[:, 0].flateen().A[0])
#     ax.scatter(xMat[:, 1].flatten().A[0)
#     plt.show()



def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T * xMat

    x, y = shape(xTx)
    print("转置矩阵的信息： x = %d; y = %d" % (x, y))

    m, n = shape(xMat)
    print("自变量的信息： m = %d; n = %d" % (m, n))

    p, q = shape(yMat)

    print("因变量的信息： p = %d; q = %d" % (p, q))

    if linalg.det(xTx) == 0.0:
        print("This Matrix is singular, cnannot do inverse")
        return

    ws = xTx.I * (xMat.T * yMat)
    return ws

def panitws(xArr, yArr):
    ws = standRegres(xArr, yArr)
    xMat = mat(xArr)
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xCopy[:,1], yHat)
    plt.show()

    yHat = xMat * ws
    print(corrcoef(yHat.T, mat(yArr)))

# def lwlr(testPoint, xArr, yArr, k = 1.0):
#     xMat = mat(xArr); yMat = mat(yArr)
#     m = shape(xMat)[0]
#     weights = mat(eye((m))) # fix me
#
#     for j in range(m):
#         diffMat = testPoint - xMat[j,:]
#         weights[j, j] = exp(diffMat * diffMat.T / (-2.0  * k ** 2))
#
#     xTx = xMat.T * (weights * xMat)
#
#     if linalg.det(xTx) == 0.0:
#          return
#
#     ws = xTx.I * (xMat.T * (weights * yMat))
#
#     return testPoint * ws


def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))

    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]     #
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))

    print(ws)

    print(testPoint)
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k = 1.0):
    m = shape(testArr)[0]

    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)

    return yHat



def ridgeRegre(xMat, yMat, lam = 0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam

    if (linalg.det(denom) == 0.0):
        print("This Matrix is singular, cannot do inverse")
        return
    ws = denom.I * (xMat.T * yMat)
    return ws


def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegre(xMat, yMat, exp(i - 10))
        wMat[i, :] = ws.T
    return wMat



def stageWist(xArr, yArr, eps = 0.01, numIt = 100):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m, n = shape(xMat)
    returnMat = zeros((numIt, n))
    ws = zeros((n, 1))
    wsTest = ws.copy()
    wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        lowestError = inf
        for j in range(n):
            for sign in [-1, 1]:
                wsTest = ws.copy()
                wsTest[j] += eps * sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.T, yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest

        ws = wsMax.copy()
        returnMat[i, :] = ws.T

    return  returnMat


def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
    myAPIstr = 'AIzaSyD2cR2KFyx12hXu6PFU-wrWot3NXvko8vY'
    searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json' % (
    myAPIstr, setNum)
    pg = urllib.request.urlopen(searchURL)
    retDict = json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem = retDict['items'][i]
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else:
                newFlag = 0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if sellingPrice > origPrc * 0.5:
                    print
                    ("%d\t%d\t%d\t%f\t%f" % (yr, numPce, newFlag, origPrc, sellingPrice))
                    retX.append([yr, numPce, newFlag, origPrc])
                    retY.append(sellingPrice)
        except:
            print('problem with item %d' % i)


def setDataCollect(retX, retY):
    searchForSet(retX, retY, 8288, 2006, 800, 49.99)
    searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
    searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
    searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
    searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
    searchForSet(retX, retY, 10196, 2009, 3263, 249.99)


if __name__ == "__main__":

    xArr, yArr = loadDataSet('ex0.txt')
    # print(xArr[0:3])
    # ws = standRegres(xArr, yArr)
    # print(ws)
    # panitws(xArr, yArr)

    # ws = lwlr(xArr[0], xArr, yArr, 1.0)
    #
    # yHat = lwlrTest(xArr, xArr, yArr, 0.01)
    #
    # print(ws)
    #
    # xMat = mat(xArr)
    # yMat = mat(yArr).T
    # srtInd = xMat[:,1].argsort(0)
    #
    # xSort = xMat[srtInd][:, 0,:]
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(xSort[:,1], yHat[srtInd])
    # ax.scatter(xMat[:,1].flatten().A[0], yMat.flatten().A[0], s =  2, c ='red')
    # plt.show()

    lgX = []; lgY = []

    setDataCollect(lgX, lgY)

