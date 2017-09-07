
from sklearn.feature_extraction import DictVectorizer


def dataextract():
    measurements = [{'city': 'adubai',  'color': 'black','temperature':33.},
                    {'city': 'shanghai', 'color': 'red', 'temperature': 12.},
                    {'city': 'beijing', 'color': 'yellow','temperature':18.},
                    {'city': 'wuhan', 'color': 'blue','temperature': 100.},
                    {'city': 'wuhan', 'color': 'white ','temperature': 100.}]
    vec = DictVectorizer()

    t = vec.fit_transform(measurements)
    print(t.toarray())

    print(vec.get_feature_names())

if __name__ == '__main__':
    dataextract()