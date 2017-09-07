from sklearn import  preprocessing
import  numpy as np


def scaleData(X):

    X_scaled = preprocessing.scale(X)

    return X_scaled

def normalizeDat(X):

    X_normalized = preprocessing.normalize(X, norm='l2')
    return X_normalized


def normalizeDat2(X):
    min_max_scaler = preprocessing.MinMaxScaler()
    x_train_minmax = min_max_scaler.fit_transform(X)
    return x_train_minmax


if __name__ == "__main__":
    X = np.array([[1., -1., 2.],
                  [2., 0., 0.],
                  [0., 1., -1.]])

    X_scaled =scaleData(X)

    print(X_scaled)

    X_normalized = normalizeDat(X)

    print(X_normalized)

    X_normalized2 = normalizeDat2(X)

    print(X_normalized2)