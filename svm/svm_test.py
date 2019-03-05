from sklearn import svm
from sklearn import  datasets
from sklearn.externals import joblib
import  pickle

clf = svm.SVC(gamma='scale')
iris = datasets.load_iris()
x ,y = iris.data, iris.target
clf.fit(x, y)
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
c = clf2.predict([x[0]])
print(c)
print(y[0])
joblib.dump(clf, 'svm.pk1')
clf3 = joblib.load('svm.pk1')
d = clf3.predict([x[1]])
print(d)
print(y[1])
