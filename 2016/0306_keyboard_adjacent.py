#!/usr/bin/env python
"""
NPR 2016-03-06

http://www.npr.org/2016/03/06/469327504/five-letters-with-which-to-play-heres-a-puzzle-to-blow-you-away

Bail, Nail, and Mail are three four-letter words that differ only by their first letters. 
And those first letters (B, N, and M) happen to be adjacent on a computer keyboard. 
Can you think of five four-letter words that have the same property -- 
that is, they're identical except for their first letters, with those first letters being adjacent on the keyboard? 
All five words must be ones that everyone knows. Capitalized words and plurals are not allowed. What words are they?
"""

from nltk.corpus import brown
from collections import defaultdict

common_words = set([x.lower() for x in brown.words() if len(x) == 4])
# Group words by last three letters
d = defaultdict(set)
for w in common_words:
    d[w[1:]].add(w[0])

# Rows on a keyboard
rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
adjacent_five = []
for row in rows:
    for i in range(len(row)-4):
        adjacent_five.append(row[i:i+5])

#%% 
for k,v in d.iteritems():
    if len(v) >= 5:
        for five in adjacent_five:
            if set(five).issubset(v):
                for first_letter in five:
                    print first_letter + k,
                print