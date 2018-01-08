#!/usr/bin/env python
"""
NPR 2017-12-31
https://www.npr.org/2017/12/31/574287856/sunday-puzzle-new-names-in-the-news

Name a famous singer — 3 letters in the first name, 5 letters in the last. 
Drop the middle letter of the last name and rearrange the result to name a 
variety of singing group. What is it?
"""
#%%
import sys
sys.path.append('..')

from nprcommontools import get_famous_names, sort_string
from nltk.corpus import wordnet as wn

singing_groups = dict()
for x in wn.all_lemma_names():
    ss = sort_string(x.replace('_','').lower())
    if len(ss) == 7:
        singing_groups[ss] = singing_groups.get(ss,[]) + [x]

names = [x for x in get_famous_names(80).keys() if x.count(' ') == 1]
names = [x for x in names if len(x.split(' ')[0])==3 and len(x.split(' ')[1])==5]

for name in names:
    fn,ln = name.lower().split(' ')
    ln = ln[:2] + ln[-2:]
    if sort_string(fn+ln) in singing_groups:
        print name, singing_groups[sort_string(fn+ln)]