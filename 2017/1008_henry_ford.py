#!/usr/bin/env/python
"""
NPR 2017-10-08

"""
import sys
sys.path.append('..')
from nprcommontools import get_synonyms

from nltk.corpus import wordnet as wn, brown, stopwords, gazetteers
from nltk import FreqDist
from math import log
import itertools
#%%

stop_words = frozenset(stopwords.words('english'))

# Code to split a letter string
# via http://stackoverflow.com/a/11642687

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
brown_words = [_.lower() for _ in brown.words()]
fdist = FreqDist(brown_words)
# "words" is a list, sorted by frequency
words = []
word_dict = dict()
NUM_WORDS = 50000
for word, frequency in fdist.most_common(NUM_WORDS):
    # Keep only the best short words
    if len(word) > 2 or word in ('a','i') or fdist[word] > 500:
        words.append(word)
        word_dict[word] = frequency
    
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

#%%
# Country names
countries = set([country.lower() for filename in ('isocountries.txt','countries.txt') \
                    for country in gazetteers.words(filename)])
    
#%%
# Words associated with Henry Ford
ford_words = set(_ for _ in get_synonyms('car') if '_' not in _)
ford_words.add('car')

good_countries = frozenset([c for w in ford_words for c in countries if w in c])
#%%
def sentence_score(s):
    """
    Score a sentence based on how common its words are
    """
    score = 0
    for w in s.split(' '):
        if w not in stop_words:
            score += word_dict.get(w,0)
    return score

#%%
sentences = dict()
for country in good_countries:
    for i in range(len(country)+1):
        no_space_sentence = country[:i] + 'e' + country[i:]
        sentence = infer_spaces(no_space_sentence)
        sentences[sentence] = sentence_score(sentence)
        
for s in sorted(sentences,key=sentences.get,reverse=True):
    print '{0} ({1})'.format(s,sentence_score(s))
    #print sentence_score(s)
