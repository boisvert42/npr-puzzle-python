#!/usr/bin/python
'''
NPR 2017-12-17
https://www.npr.org/2017/12/17/571421849/sunday-puzzle-capital-letters

Think of a convenience introduced in the 19th century that is still around today. 
Its name has two words. Take the first three letters of the first word and the 
first letter of its second word, in order, to get a convenience introduced in the 
21st century that serves a similar purpose. Their names are otherwise unrelated. 
What two conveniences are these?
'''

from nltk.corpus import wordnet as wn

from nltk.tokenize import word_tokenize
from nltk import FreqDist

import sys
sys.path.append('..')
from nprcommontools import get_hypernyms

#%%
# "common" words from Wordnet
# We use words in example sentences
def_corpus = []
for s in wn.all_synsets():
    for ex in s.examples():
        for w in word_tokenize(ex):
            if w.isalpha():
                def_corpus.append(w.lower())
            
fdist = FreqDist(def_corpus)
common_words = set()
NUM_WORDS = 50000
for word, frequency in fdist.most_common(NUM_WORDS):
    # Keep only the best short words
    if len(word) > 2 or word in ('a','i') or fdist[word] > 100:
        common_words.add(word)

#%%
four = set()
two_words = set()
for s in wn.all_synsets():
    if s.pos() == 'n':
        for l in s.lemma_names():
            if l[0] != l[0].upper():
                if len(l) == 4 and '_' not in l and l in common_words:
                    four.add(l)
                elif l.count('_') == 1 and l.split('_')[0] in common_words and l.split('_')[1] in common_words:
                    if 'product' in get_hypernyms(l):
                        two_words.add(l)
        
#%%
for t in sorted(two_words):
    w1,w2 = t.split('_')
    if w1[:3] + w2[0] in four:
        print t,w1[:3] + w2[0]


