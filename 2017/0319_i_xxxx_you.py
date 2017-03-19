#!/usr/bin/env python
"""
NPR 2017-03-19
http://www.npr.org/2017/03/19/520595633/sunday-puzzle-youll-need-to-unscramble-the-opposition
Think of a familiar phrase in the form "I ___ you," in which a four-letter word goes in the blank. 
Rearrange those letters and you'll get another familiar phrase in the form "I ___ you." 
Both phrases get more than half a million hits in a Google search. What phrases are these?
"""

# Note: this doesn't actually give the correct answer

import sys
sys.path.append('..')
from nprcommontools import sort_string
from nltk.corpus import movie_reviews,brown,webtext,reuters,gutenberg, nps_chat
#from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter, defaultdict

#%%
middle_words = set()
for module in [movie_reviews,brown,webtext,reuters,gutenberg,nps_chat]:
    trigrams = ngrams(module.words(), 3)
    trigrams_freq = Counter(trigrams)
    s = set([x[1] for x in trigrams_freq if x[0].lower() == 'i' and x[2].lower() == 'you' and len(x[1]) == 4])
    middle_words = middle_words.union(s)
print middle_words
#%%
sorted_words = defaultdict(list)
for word in middle_words:
    s = sort_string(word)
    if s in sorted_words:
        print word,sorted_words[s]
    sorted_words[s].append(word)

