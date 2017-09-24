#!/usr/bin/env python
"""
NPR 2017-09-10

Think of a famous quotation with 8 words. 
The initial letters of the first 4 words themselves spell a word, 
and the initial letters of the last 4 words spell another word. 
Both words rhyme with "jab." What quotation is it?
"""

import sys
sys.path.append('..')
import rhyme
from nltk.corpus import brown, wordnet as wn

brown_words = frozenset(brown.words())

#%%
# Check out words that rhyme with "jab"
rhymes_with_jab = [x for x in rhyme.all_rhymes('jab') if len(x) == 4]

# Last word starts and ends with "b", second-to-last with "a"
# (unless "sabb", "tabb", and "nabb" are common words)
b_words = [x for x in wn.all_lemma_names() if x.startswith('b') and x.endswith('b')  and x.isalpha()]
#print [x for x in brown_words if x.startswith('a') and x.endswith('a')]

for w in b_words:
    print [x for x in wn.all_lemma_names() if x.endswith('_{0}'.format(w)) and x.count('_') == 3]
