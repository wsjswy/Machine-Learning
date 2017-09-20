
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import  CountVectorizer


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

def datattimes():

    vectorizer = CountVectorizer(min_df=1)
    print(vectorizer)
    corups = [
        'This is the first document',
        'This is the second second document',
        'And the third one',
        'Is this the first document',
    ]

    X = vectorizer.fit_transform(corups)

    print(type(X))

    print(vectorizer.get_feature_names())

if __name__ == '__main__':
    datattimes()