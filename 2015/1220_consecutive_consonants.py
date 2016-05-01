#!/usr/bin/env python
'''
NPR 2015-12-20

http://www.npr.org/2015/12/20/460421632/yule-never-guess-the-theme-to-this-weeks-song-filled-puzzle

Think of four common six-letter words that all end in the same five letters, in the same order. 
And the first letters of these four words are consecutive consonants in the alphabet (like B, C, D, F). 
No other common six-letter words end with these five letters. What are the words?
'''

from nltk.corpus import gutenberg
from collections import defaultdict

words = frozenset([x.lower() for x in gutenberg.words() if len(x) == 6 and x.isalpha()])

consonants = 'bcdfghjklmnpqrstvwxz'
consecutive_consonants = set()
for i in range(len(consonants)-3):
    consecutive_consonants.add(frozenset(consonants[i:i+4]))

letter_dict = defaultdict(set)
for word in words:
    last_letters = word[1:]
    letter_dict[last_letters].add(word[0])
    
for k,v in letter_dict.iteritems():
    if v in consecutive_consonants:
        for letter in sorted(v):
            print letter + k,
        print