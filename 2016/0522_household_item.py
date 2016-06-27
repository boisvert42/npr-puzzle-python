#!/usr/bin/env python
'''
NPR 2016-05-22

http://www.npr.org/2016/05/22/478980646/straight-out-of-the-funny-papers-here-are-a-few-cartoon-conundrums

Name a common household item in 6 letters. Change the middle two letters to a P, 
and you'll get the 5-letter last name of a famous person who professionally used that item. 
What's the item, and who's the person?
'''

import sys
sys.path.append('..')
import nprcommontools as nct
from collections import defaultdict
from nltk.corpus import brown

common_words = frozenset([_x.lower() for _x in brown.words()])

household_objects = [_x for _x in nct.get_category_members('physical_object') \
    if len(_x) == 6 and _x == nct.alpha_only(_x) and _x in common_words]
        
last_to_name = defaultdict(list)
names = nct.get_famous_names(95)
for name in names:
    if name.find(' ') > 0:
        split_names = name.split(' ')
        if len(split_names[-1]) == 5 and split_names[-1][2] == 'p':
            last_to_name[split_names[-1].lower()].append(name)
last_names = frozenset(last_to_name.keys())
            
#%%
for obj in household_objects:
    name = obj[:2] + 'p' + obj[4:]
    if name in last_names:
        print obj, last_to_name[name]