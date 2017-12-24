#!/usr/bin/env python
"""
NPR 2017-12-24
https://www.npr.org/2017/12/24/572833897/sunday-puzzle-initially-you-might-be-right-but-its-time-to-switch-it-up

The name of what well-known U.S. city, in 10 letters, contains only three different letters of the alphabet?
"""
#%%
from nltk.corpus import wordnet as wn

for l in wn.all_lemma_names():
    l2 = l.replace('_','').lower()
    if len(l2) == 10 and len(set(l2)) == 3:
        syns = wn.synsets(l)
        for syn in syns:
            d = syn.definition()
            if 'city' in d or 'town' in d:
                print l