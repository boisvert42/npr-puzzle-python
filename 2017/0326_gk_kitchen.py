#!/usr/bin/python
'''
NPR 2017-03-26
http://www.npr.org/2017/03/26/521446835/sunday-puzzle-keep-the-bookend-letters-from-these-words-to-make-new-ones
Name two things found in a kitchen — one starting with G, the other starting with K. 
If you have the right ones, you can rearrange the letters to name two other things, 
one of them found in the kitchen starting with F, the other one probably found elsewhere 
in the house starting with K. What things are these?
'''
import sys
sys.path.append('..')
from nprcommontools import get_category_members, sort_string
from itertools import combinations
from collections import defaultdict
from nltk.corpus import brown
#%%
common_words = frozenset(brown.words())
objects = [x for x in get_category_members('object') if x in common_words]
object_pairs = [x for x in combinations(objects,2) if x[1].startswith('k')]

#%%
fk_pairs = defaultdict(list)
fk_ss = set()
gk_pairs = defaultdict(list)
gk_ss = set()

#%%
for pair in object_pairs:
    ss = sort_string(pair[0]+pair[1])
    if pair[0].startswith('g'):
        gk_pairs[ss].append(pair)
        gk_ss.add(ss)
    elif pair[0].startswith('f'):
        fk_pairs[ss].append(pair)
        fk_ss.add(ss)

#%%
for ss in fk_ss.intersection(gk_ss):
    print gk_pairs[ss], fk_pairs[ss]