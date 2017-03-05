#!/usr/bin/env python
"""
NPR 2017-03-05
http://www.npr.org/2017/03/05/518606016/here-is-a-challenge-to-hear-and-write-the-right-answer
Write the name of a game in small letters. Reverse the second and third letters. 
Turn the fourth letter upside-down. The result will name something else to play. What is it?
"""

import sys
sys.path.append('..')
from nprcommontools import alpha_only
from nltk.corpus import brown
#%%
# Common words from Brown corpus
words = frozenset([_ for _ in brown.words() if _ == _.lower() and len(_) >= 4 and _ == alpha_only(_)])

#%%
# Upside-down letter dict
letter_dict = {'e':'a','a':'e','w':'m','m':'w','r':'j',
               'u':'n','n':'u','p':'d','d':'p','q':'b','b':'q',
               'h':'y'}
possible_letters = frozenset(letter_dict.keys())
#%%
for w in words:
    try:
        if w[2] == w[1]:
            continue
        w2 = w[0] + w[2] + w[1] + letter_dict[w[3]] + w[4:]
        if w2 in words:
            print w,w2
    except KeyError:
        pass