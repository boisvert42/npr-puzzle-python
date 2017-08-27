#!/usr/bin/env python
"""
NPR 2017-08-27
http://www.npr.org/2017/08/27/545580069/sunday-puzzle-categorically-speaking
This week's challenge is a common two-word expression. 
The expression consists of 8 letters and uses all five vowels — A, E, I, O and U. 
It has only three consonants, one of which is repeated. 
The first word in the expression has two letters and the second has six letters. 
What familiar expression is it?
"""

from nltk.corpus import wordnet as wn

#%%
for word in wn.all_lemma_names():
    if len(set(word).intersection(set('aeiou'))) == 5 and len(word) == 9 and word[2] == '_':
        print word
