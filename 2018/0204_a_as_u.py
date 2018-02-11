#!/usr/bin/env python
"""
NPR 2018-02-04
https://www.npr.org/2018/02/04/582750978/sunday-puzzle-stuck-in-the-middle

In English, a short "u" sound is usually spelled with a "u," as in "fun" and "luck." 
Occasionally it's spelled with an "o," as in "come" and "love." 
Can you name two everyday one-syllable words in which a short "u" sound is 
spelled with an "a"?
"""
from nltk.corpus import cmudict
cdict = cmudict.dict()

#%%
for word in cdict.iterkeys():
    if 'a' in word:
        for p in cdict[word]:
            if 'AH1' in p and sum([c.isdigit() for c in ''.join(p)]) == 1:
                print word
