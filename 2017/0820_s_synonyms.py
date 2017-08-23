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

from nltk.corpus import wordnet as wn, brown

def is_adjective(word):
    ''' Check if the word is an adjective, per Wordnet '''
    syns = wn.synsets(word)
    for s in syns:
        if s.pos() == 'a':
            return True
    return False

brown_words = frozenset(x for x in brown.words() if len(x) == 5 and x.isalpha() and x.startswith('s'))
#%%
# We'll just print all five-letter adjectives beginning with S and go by inspection.
for word in brown_words:
    if is_adjective(word):
        print word
        
