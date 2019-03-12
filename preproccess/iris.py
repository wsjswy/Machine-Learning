from sklearn import datasets
import numpy as np
from  sklearn.preprocessing import  MinMaxScaler
from  sklearn.preprocessing import  StandardScaler
from  sklearn.preprocessing import  Normalizer
from  sklearn.preprocessing import  Binarizer

data = datasets.load_iris()
X, y = data.data, data.target

# np.set_printoptions(precision=3)
print ("\n" "Preprocess input variables: " "\n")
print ("Raw Data: ")
print (X[:5, :])

#尺度变换
X1 = data.data
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X1)
print ("\nRescaled Data: ")
print(rescaledX[0:5,:])

#标准化
scaler = StandardScaler().fit(X1)
standardizedX = scaler.fit_transform(X1)


#正规化
scaler = Normalizer().fit(X)
normalizedX = scaler.fit_transform(X)

#二值化


