#!/usr/bin/env python
"""
NPR 2017-01-29
http://n.pr/2kB56SQ
Take six different letters. Repeat them in the same order.
Then repeat them again - making 18 letters altogether.
Finally add "tebasket" at the end. If you have the right
letters and you space them appropriately, you'll complete
a sensible sentence.  What is it?
"""

from math import log
from nltk.corpus import brown
from nltk import FreqDist
import itertools
#%%
# Code to split a letter string
# Thanks http://stackoverflow.com/a/11642687

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
brown_words = [_.lower() for _ in brown.words()]
fdist = FreqDist(brown_words)
# "words" is a list, sorted by frequency
words = []
NUM_WORDS = 50000
for word, frequency in fdist.most_common(NUM_WORDS):
    # Keep only the best short words
    if len(word) > 2 or word in ('a','i') or fdist[word] > 500:
        words.append(word)

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
# Let's assume that our string will end with "wastebasket"
# Because why put "tebasket" at the end otherwise?
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for abc in itertools.permutations(alphabet,3):
    a,b,c = abc
    s = (a+b+c+'was')*3+'tebasket'
    s2 = infer_spaces(s)
    if s2.endswith('wastebasket') \
    and s2[:7] != s2[8:15] \
    and s2[:8] != s2[9:17] \
    and s2[:9] != s2[10:19]:
        print s2