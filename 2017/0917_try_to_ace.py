#!/usr/bin/env python
"""
NPR 2017-09-17

http://www.npr.org/2017/09/17/551562686/sunday-puzzle-three-words-two-homophones-one-conjunction

Think of two antonyms, each in three letters. Set them side by side. 
In between them arrange the letters of TRY TO ACE in some order. 
The result will name someone at school. Who is it?
"""

import sys
sys.path.append('..')
from nprcommontools import alpha_only, sort_string
from nltk.corpus import wordnet as wn

#%%
sorted_key_string = sort_string('trytoace')
for w in wn.all_lemma_names():
    w2 = alpha_only(w.lower())
    if len(w2) == len(sorted_key_string) + 6:
        if sort_string(w2[3:-3]) == sorted_key_string:
            print w