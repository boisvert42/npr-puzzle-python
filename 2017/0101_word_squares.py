#!/usr/bin/env python
"""
NPR 2017-01-01
http://www.npr.org/2017/01/01/507567187/for-this-puzzling-retrospective-on-2016-youll-need-a-set-of-speakers
Take the four-letter men's names TODD, OMAR, DAVE and DREW. 
If you write them one under the other, they'll form a word square, spelling TODD, OMAR, DAVE and DREW reading down as well:
TODD
OMAR
DAVE
DREW

Can you construct a word square consisting of five five-letter men's names? 
Any such square using relatively familiar men's names will count. 
I have an answer using four relatively common names and one less familiar one.
"""

from nltk.corpus import names
from collections import defaultdict
#%%
NAME_LENGTH = 5

all_names = set([x.lower() for x in names.words('male.txt')])
my_names = frozenset(x for x in all_names if len(x) == NAME_LENGTH)

# Thanks https://discuss.leetcode.com/topic/63428/short-python-c-solution
def wordSquares(words):
    n = NAME_LENGTH
    fulls = defaultdict(list)
    for word in words:
        for i in range(n):
            fulls[word[:i]].append(word)
    def build(square):
        if len(square) == n:
            squares.append(square)
            return
        for word in fulls[''.join(zip(*square)[len(square)])]:
            build(square + [word])
    squares = []
    for word in words:
        build([word])
    return squares
    
squares = wordSquares(my_names)
for s in squares:
    for i in range(len(s)):
        print s[i],
    print
