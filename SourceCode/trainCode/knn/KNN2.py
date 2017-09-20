import  sys
import  urllib
import  re
import  numpy as np
from sklearn.externals import joblib
import  csv
import  matplotlib.pyplot as plt
from  sklearn.feature_extraction.text import  CountVectorizer
from  sklearn.neighbors import  KNeighborsClassifier
from  nltk.probability import  FreqDist

N = 90
MIN_LEN = 1

def load_alexa(filename):

    domain_list = []
    csv_reader = csv.reader(open(filename))
    for row in csv_reader:
        domain = row[1]
        if domain >= MIN_LEN:
            domain_list.append(domain)

    return domain_list

def domain2ver(domain):

    ver = []

    for i in range(0, len(domain)):
        ver.append([ord(domain[i])])
    return ver


def load_user_cmd(fileName):

        cmd_list = []
       # dist_max = []
       # dist_min = []
        dist = []

        with open(fileName) as f:
            i = 0
            x = []
            for line in f:
                line = line.strip('\n')
                x.append(line)
                dist.append(line)
                i += 1
                if i == 100:
                    cmd_list.append(x)
                    x = []
                    i = 0
        fdist = list(FreqDist(dist).keys())


        print(type(fdist))

        dist_max = set(fdist[0:50])
        dist_min = set(fdist[-50:0])

        return  cmd_list, dist_max, dist_min

def get_user_cmd_feature(user_cmd_list, dist_max, dist_min):

    user_cmd_feature = []
    for cmd_block in user_cmd_list:
        f1 = len(set(cmd_block))
        fdist = list(FreqDist(cmd_block).keys())
        f2 = fdist[0:10]
        f3 = fdist[-10:0]

        f2 = len(set(f2) & set(dist_max))
        f3 = len(set(f3) & set(dist_min))
        x = [f1, f2, f3]

        user_cmd_feature.append(x)

    return user_cmd_feature

def get_label(fileName, index = 0):
    x = []

    with open(fileName) as f:
        for line in f:
            line = line.strip('\n')
            x.append(int(line.split()[index]))

    return x

if __name__ == '__main__':

    root_path = '/Users/wsjswy/Documents/github/machineLearning/SourceCode/trainCode/knn/MasqueradeDat/'

    user_cmd_list, user_cmd_dist_max, user_cmd_dist_min = load_user_cmd(root_path +'User3')
    user_cmd_feature = get_user_cmd_feature(user_cmd_list, user_cmd_dist_max, user_cmd_dist_min)

    labels = get_label(root_path + 'label.txt', 2)
    y = [0] * 50 + labels

    x_train = user_cmd_feature[0: N]
    y_train = y[0:N]

    x_test = user_cmd_feature[N:150]
    y_test = y[N:150]

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x_train, y_train)

    y_predict = neigh.predict(x_test)

    score = np.mean(y_test == y_predict) * 100

    print(y_test)

    print(y_predict)

    print(score)