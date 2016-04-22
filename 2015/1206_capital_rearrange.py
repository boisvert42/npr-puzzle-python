#!/usr/bin/env python
'''
NPR 2015-12-06

http://www.npr.org/2015/12/06/458661972/transform-words-with-an-additional-letter-in-this-weeks-puzzle

Name a state capital. Drop one of its letters. 
The remaining letters can be rearranged to name of another major city 
in the United States. What is it? 
There are two different answers, and you should find both of them.
'''

import sys
sys.append('..')
from nprcommontools import sort_string

from nltk.corpus import wordnet as wn, gazetteers
import re

# U.S. States
states = set(gazetteers.words('usstates.txt'))

# capitals and major cities
cities = set(); capitals = set()
for synset in wn.all_synsets():
    d = synset.definition()
    for state in states:
        if state in d and 'city' in d:
            for l in synset.lemma_names():
                if l[0] == l[0].upper():
                    cities.add(l)
        if state in d and 'capital' in d:
            for l in synset.lemma_names():
                if l[0] == l[0].upper():
                    capitals.add(l)

sorted_cities = dict([(sort_string(re.sub(r'[^a-z]+','',city.lower())),city) for city in cities])
sorted_keys = frozenset(sorted_cities.keys())
#%%
# thank you http://norvig.com/spell-correct.html
def deletes(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]   
    return set([sort_string(x) for x in deletes])               
                    
for capital in capitals:
    cap2 = re.sub(r'[^a-z]+','',capital.lower())
    if not deletes(cap2).isdisjoint(sorted_keys):
        keys = deletes(cap2).intersection(sorted_keys)
        for key in keys:
            print capital,sorted_cities[key]