__author__ = 'wsjswy'

import  bayes2

listOPosts, listClasses = bayes2.loadDataSet()

myVocabList = bayes2.createVocabList(listOPosts)

print(myVocabList)

print(bayes2.setOfWords2Vec(myVocabList, listOPosts[0]))

print(bayes2.setOfWords2Vec(myVocabList, listOPosts[1]))



