#!/usr/bin/env python
"""
NPR 2016-02-28

http://www.npr.org/2016/02/28/468417481/and-this-puzzles-winner-is

What two 8-letter terms in math are anagrams of each other? 
One word is from geometry, the other is from calculus. What words are they?
"""

# We take words that appear in numpy docstrings as a proxy for "math terms"
import numpy as np
from nltk.tokenize import word_tokenize
from collections import defaultdict

eight_letter_math_terms = defaultdict(set)
docstrings = [getattr(np,method).__doc__ for method in dir(np) if callable(getattr(np, method))]
for d in docstrings:
    if d is not None:
        word_list = [x.lower() for x in word_tokenize(d) if len(x) == 8 and x.isalpha()]
        for word in word_list:
            eight_letter_math_terms[''.join(sorted(word))].add(word)


print [', '.join(v) for v in eight_letter_math_terms.itervalues() if len(v) >= 2]