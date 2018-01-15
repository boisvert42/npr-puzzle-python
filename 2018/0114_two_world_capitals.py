#!/usr/bin/env python
"""
NPR 2018-01-14
https://www.npr.org/2018/01/14/577363065/sunday-puzzle-a-twisted-ending

Name a world capital. It's an older way of spelling the name. 
Drop three letters, and the remaining letters, in order, will name another world capital. 
Both cities have more than a million residents. What cities are these?
"""

from nltk.corpus import wordnet as wn

def w1_in_w2_in_order(w1,w2):
    if w1 == w2:
        return False
    for c in w1:
        ix = w2.find(c)
        if ix == -1:
            return False
        w2 = w2[ix+1:]
    return True
#%%
capitals = set()
for s in wn.all_synsets():
    if 'capital' in s.definition() and 'city' in s.definition():
        for l in s.lemma_names() :
            if l[0].upper() == l[0]:
                capitals.add(l)
            
#%%
for c1 in capitals:
    for c2 in capitals:
        if w1_in_w2_in_order(c1,c2) and len(c2) == len(c1) + 3:
            print c1,c2