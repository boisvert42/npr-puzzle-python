#!/usr/bin/env python
"""
NPR 2016-01-17

http://www.npr.org/2016/01/17/463333521/it-may-be-topsy-turvy-but-this-puzzle-still-invites-categorization?utm_medium=RSS&utm_campaign=sundaypuzzle

Think of a category in three letters in which the last 
two letters are the first two letters of something in that 
category. And the thing in the category has seven letters. 
Both names are common, uncapitalized words. What are they?
"""
import sys
sys.path.append('..')
from nprcommontools import get_category_members

from nltk.corpus import wordnet as wn

three = [x for x in wn.all_lemma_names() if len(x) == 3]

for word in three:
    poss = [x for x in get_category_members(word) if x[:2] == word[-2:] and len(x) == 7]
    if poss:
        print word,poss