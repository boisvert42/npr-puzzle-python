#!/usr/bin/python
'''
NPR 2017-07-09
http://www.npr.org/2017/07/09/535952970/sunday-puzzle-switch-it-up

Take a certain 7-letter word. Remove the first letter and you get 
a 6-letter synonym of that word. And the letter you removed is an 
abbreviation for the opposite of both words. What words are these?
'''
import sys
sys.path.append('..')
from nprcommontools import get_synonyms
from nltk.corpus import brown

#%%
words = frozenset([_.lower() for _ in brown.words() if _.isalpha() and len(_) == 7])

#%%
for seven in words:
    syns = get_synonyms(seven)
    if seven[1:] in syns:
        print seven, seven[1:], seven[0]