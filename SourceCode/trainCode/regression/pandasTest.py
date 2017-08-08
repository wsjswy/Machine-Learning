
import  pandas

from  sklearn import  naive_bayes

from  sklearn import  datasets;



def pandasFun():

    dataInfo = pandas.read_fwf("brain_body.txt")

    x_values = dataInfo['Brain']
    y_values = dataInfo['Body']

    return  x_values, y_values



def bayesTest():
    iris = datasets.load_iris()

    gnb = naive_bayes.GaussianNB()

    trainData = gnb.fit(iris.data, iris.target)

    y = trainData.predict(iris.data)


    print(iris.data.shape[0])




if  __name__ == "__main__":

    x, y = pandasFun();

    len = len(x)



    bayesTest()