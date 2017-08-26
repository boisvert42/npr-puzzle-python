#!/usr/bin/env python
"""
NPR 2017-08-20
http://www.npr.org/2017/08/20/544126301/sunday-puzzle-its-time-to-rhyme
Think of two synonyms — one in 5 letters, the other in 4. 
The 5-letter word starts with S. The 4-letter word contains an S. 
Change one of these S's to an A. You can rearrange the result to name 
a group of people, in 9 letters, that ideally have those two adjectives 
describe them. What group is it?
"""
import sys
sys.path.append('..')
from nprcommontools import alpha_only, sort_string, get_synonyms
from nltk.corpus import wordnet as wn, brown
from collections import defaultdict

def is_adjective(word):
    ''' Check if the word is an adjective, per Wordnet '''
    syns = wn.synsets(word)
    for s in syns:
        if s.pos() in ('a','s'):
            return True
    return False

words5 = frozenset(x for x in brown.words() if len(x) == 5 and x.isalpha() and x.startswith('s') and is_adjective(x))
words4 = frozenset(x for x in brown.words() if len(x) == 4 and x.isalpha() and 's' in x and is_adjective(x))
words9 = dict((sort_string(alpha_only(x)),x) for x in wn.all_lemma_names() if len(alpha_only(x)) == 9)
#%%
for word in sorted(words5):
    syns = get_synonyms(word)
    for syn in syns.intersection(words4):
        s1 = sort_string('a' + word[1:] + syn)
        #if s1:
        #    print word, syn
        try:
            new_word = words9[s1]
            print word, syn, new_word
        except KeyError:
            pass
