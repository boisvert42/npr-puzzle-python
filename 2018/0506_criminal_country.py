#!/usr/bin/python
'''
NPR 2018-05-06

https://www.npr.org/2018/05/06/607707509/sunday-puzzle-in-d-mood-for-a-game

Name a certain kind of criminal. 
Drop the first two letters and the last letter of the word, and you'll name a country. 
What is it?
'''
from nltk.corpus import wordnet as wn, gazetteers
        
#%%
COUNTRIES = set([country.lower() for filename in ('isocountries.txt','countries.txt')
  for country in gazetteers.words(filename)])

words = wn.all_lemma_names()

for w in words:
    if w[2:-1] in COUNTRIES and len(w) > 5:
        print w
