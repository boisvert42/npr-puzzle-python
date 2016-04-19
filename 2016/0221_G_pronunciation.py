#!/usr/bin/env python
"""
NPR 2016-02-21

http://www.npr.org/2016/02/21/467515215/the-phrase-or-name-is-familiar-try-this-puzzle-and-see-what-they-are

Think of three eight-letter words that are identical in spelling except for the fourth letter. 
Each word contains a G ... that is pronounced differently in all three words. What words are they?
"""

from nltk.corpus import words, brown
from collections import defaultdict

words = set([x.lower() for x in words.words() if len(x) == 8 and 'g' in x.lower() and not x.endswith('ing')])
words = words.union(set([x.lower() for x in brown.words() if len(x) == 8 and 'g' in x.lower() and not x.endswith('ing')]))

d = defaultdict(set)
for word in words:
    w2 = word[:3]+word[4:]
    d[w2].add(word)
    
for v in d.values():
    if len(v) >= 3:
        print v
