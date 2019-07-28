#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NPR 2019-07-28
https://www.npr.org/2019/07/28/745971618/sunday-puzzle-high-cs

The word BEVY is "alphabetically balanced." 
That is, the first letter, B, is second from the start of the alphabet, 
and the last letter, Y, is second from the end of the alphabet. 
Similarly, E and V are each fifth from the ends of the alphabet. 
Can you think of a six-letter word related to magic that is similarly balanced?
"""

from nltk.corpus import wordnet as wn

def is_balanced(s):
    s = s.lower()
    if len(s) % 2 == 1:
        return False
    while s:
        a, z = s[0], s[-1]
        n1, n2 = ord(a) - 97, ord(z) - 97
        if n1 + n2 != 25:
            return False
        else:
            s = s[1:-1]
    return True

for w in wn.all_lemma_names():
    if is_balanced(w):
        print(w)
