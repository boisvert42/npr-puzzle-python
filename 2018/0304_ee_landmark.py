#!/usr/bin/env python
"""
NPR 2018-03-04
https://www.npr.org/2018/03/04/590233321/sunday-puzzle-o-s-c-a-r
Name a famous singer — first and last names. 
Change the last three letters of each name to an E and you'll name 
a well-known landmark. What is it?
"""

import sys
sys.path.append('..')
import nprcommontools as nct
from nltk.corpus import wordnet as wn
ee_words = set()
for x in wn.all_lemma_names():
    if x.count('_') == 1:
        t1,t2 = x.split('_')
        if t1.endswith('e') and t2.endswith('e'):
            ee_words.add(t1+" "+t2)
names = nct.get_famous_names(95)

#%%
for name in names:
    if name.count(' ') == 1:
        n1,n2 = name.lower().split(' ')
        if len(n1) > 3 and len(n2) > 3:
            n1 = n1[:-3]+'e'; n2 = n2[:-3]+'e'
            if n1 + ' ' + n2 in ee_words:
                print name
