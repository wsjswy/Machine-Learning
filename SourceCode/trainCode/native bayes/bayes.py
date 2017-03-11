__author__ = 'wsjswy'


import  numpy as np

from  sklearn.naive_bayes import GaussianNB

X = np.array([[1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()

clf.fit(X, Y)

print(clf.predict([[1, 0.1]]))
