#!/usr/bin/env python
"""
NPR 2017-01-08
http://www.npr.org/2017/01/08/508732771/top-prize-for-solving-a-tough-puzzle-theres-a-total-pattern-here
Think of a two-word phrase you might see on a clothing label. 
Add two letters to the end of the first word, and one letter to the end of the second word. 
The result is the name of a famous writer. Who is it?
"""

import sys
sys.path.append('..')
from nprcommontools import get_famous_names
from nltk.corpus import wordnet as wn
#%%
# Famous names
MIN_NAME_SCORE = 98
names = frozenset([_.lower() for _ in get_famous_names(MIN_NAME_SCORE) if _.count(' ') == 1])

#%%
# Two-word phrases
phrases = frozenset([_.replace('_',' ') for _ in wn.all_lemma_names() if _.count('_') == 1])

#%%
for name in names:
    first_name, last_name = name.split(' ')
    first_word = first_name[:-2]; last_word = last_name[:-1]
    phrase = '{0} {1}'.format(first_word,last_word)
    if phrase in phrases:
        print name, phrase
