#!/usr/bin/env python
"""
NPR 2018-12-02

https://www.npr.org/2018/12/02/672656517/sunday-puzzle-2-words

Think of a common 7-letter word. Drop its second letter, 
and you'll get a 6-letter word that does not rhyme with the first. 
Alternatively, you can drop the third letter from the 7-letter word 
to get a 6-letter word that doesn't rhyme with either of the first two. 
Further, you can drop both the second and third letters 
from the 7-letter word to get a 5-letter word that doesn't rhyme 
with any of the others. What words are these?
"""

import sys
sys.path.append('..')
import rhyme
from nltk.corpus import brown

brown_words = frozenset(brown.words())

#%%
for x in brown_words:
    if len(x) == 7 and x.isalpha():
        w1 = x[:1] + x[2:]
        w2 = x[:2] + x[3:]
        w3 = x[:1] + x[3:]
        if w1 in brown_words and w2 in brown_words and w3 in brown_words:
            if (not rhyme.does_rhyme(x,w1)) and (not rhyme.does_rhyme(x,w2)) and (not rhyme.does_rhyme(x,w3)):
                print(x,w1,w2,w3)
