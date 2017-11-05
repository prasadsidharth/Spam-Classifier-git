#!/usr/bin/env python3


"""Naive Bayes Classifier"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:20:12 2017

@author: Sidharth
"""


import os
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
#from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

ham_train_messages = []
spam_train_messages = []
test_messages = []

#importing the training data and storing them in a lists of strings

for filename in os.listdir('train_data/ham'):

    f = open('train_data/ham/'+filename,'r',errors='ignore')
    message = f.read()
    ham_train_messages.append(str(message))
    f.close()
    
for filename in os.listdir('train_data/spam'):

    f = open('train_data/spam/'+filename,'r',errors='ignore')
    message = f.read()
    spam_train_messages.append(str(message))
    f.close()
    
#importing the testing data and storing them in a list of strings

for filename in os.listdir('test_data/'):

    f = open('test_data/'+filename,'r',errors='ignore')
    message = f.read()
    test_messages.append(str(message))
    f.close()

no_of_spam_emails = len(spam_train_messages)
no_of_ham_emails = len(ham_train_messages)
no_of_test_emails = len(test_messages)

ham_train_messages_stemmed = []
spam_train_messages_stemmed = []

#performing stemming and putting the strings back again with a ' ' b/w them

for message in spam_train_messages:
    s = message.split()
    m = []
    for i in s:
       m.append(ps.stem(i))
    spam_train_messages_stemmed.append(' '.join(m))
    
for message in ham_train_messages:
    s = message.split()
    m = []
    for i in s:
       m.append(ps.stem(i))
    ham_train_messages_stemmed.append(' '.join(m))
    
#creating the spam and ham dictionaries
    
vectorizer1 = CountVectorizer()
print(vectorizer1.fit_transform(ham_train_messages_stemmed).todense())
ham_dict = vectorizer1.vocabulary_  

vectorizer2 = CountVectorizer()
print(vectorizer2.fit_transform(spam_train_messages_stemmed).todense())
spam_dict = vectorizer2.vocabulary_  

#removing non-aplhabetic words and single letter words from the spam and ham dictionaries

len_spam_dict_init = len(spam_dict)
len_ham_dict_init = len(ham_dict)

for item in ham_dict.copy().keys():
    if item.isalpha() == False: 
        del ham_dict[item]
    elif len(item) == 1:
        del ham_dict[item]


for item in spam_dict.copy().keys():
    if item.isalpha() == False: 
        del spam_dict[item]
    elif len(item) == 1:
        del spam_dict[item]
        
len_spam_dict_f = len(spam_dict)
len_ham_dict_f = len(ham_dict)
        
#making the first change
#making the third change
    
    
    