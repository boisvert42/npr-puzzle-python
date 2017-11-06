#!/usr/bin/python
'''
NPR 2017-11-05
http://www.npr.org/2017/11/05/561980137/sunday-puzzle-whats-in-style

Think of the last name of a famous film director. 
The first two letters and last two letters in order spell a word. 
And the remaining letters, rearranged, spell a synonym of that word. 
What film director is it?
'''

import sys
sys.path.append('..')
from nprcommontools import get_famous_names, sort_string, wikipedia_category_members

from nltk.corpus import wordnet as wn

#%%
# "common" words from Wordnet
common_word_dict = dict()
common_words = set()
for s1 in wn.all_lemma_names():
    if s1.isalpha() and s1 == s1.lower():
        common_word_dict[sort_string(s1)] = common_word_dict.get(sort_string(s1),[]) + [s1]
        common_words.add(s1)
common_word_sort_set = frozenset(common_word_dict.keys())

#%%
famous_names = get_famous_names(99)
directors = wikipedia_category_members('American_film_directors', max_depth=1)

#%%
names = directors.intersection(famous_names)

for name in names:
    name2 = name.lower().split(' ')[-1]
    word = name2[:2] + name2[-2:]
    middle = sort_string(name2[2:-2])
    
    if word in common_words:
        if middle in common_word_sort_set:
            for word2 in common_word_dict[middle]:
                print name, word, word2


