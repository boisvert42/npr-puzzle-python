#!/usr/bin/env python
"""
NPR 2017-02-19
http://www.npr.org/2017/02/19/516007834/sunday-puzzle-solving-this-puzzle-might-mean-a-few-outfit-changes

Think of an article of apparel in five letters. 
Change one letter in it to name another article of apparel. 
Change one letter in that to name a third article of apparel. 
Then change one letter in that to name a fourth article of apparel. 
The position of the letters you change are different each time. 
What articles are these?
"""

import sys
sys.path.append('..')
from nprcommontools import get_hypernyms, get_category_members

#%%
# What category should we use?
print get_hypernyms('jacket')
# Looks like "article_of_clothing"

#%%
articles = set([_ for _ in get_category_members('article_of_clothing') if len(_) == 5])

# Thanks http://norvig.com/spell-correct.html

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    return set(replaces)

for article in articles:
    new_articles = [_ for _ in edits1(article) if _ in articles and _ != article]
    if new_articles:
        print article, new_articles