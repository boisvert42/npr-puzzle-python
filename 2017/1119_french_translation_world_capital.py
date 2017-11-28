#!/usr/bin/python
'''
NPR 2017-11-19
https://www.npr.org/puzzle

Think of a French expression with enumeration (3,2,5).  Its English translation
is a two-word phrase.  The first words of the two phrases sound like a world
capital.  What is it?
'''

from nltk.corpus import wordnet as wn
import re

#%%
for l in wn.all_lemma_names():
    if re.match('^.{3}_.{2}_.{5}$',l) is not None and l[4:6] != 'of':
        print l
