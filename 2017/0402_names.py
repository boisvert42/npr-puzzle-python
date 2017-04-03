#!/usr/bin/python
'''
NPR 2017-04-02
http://www.npr.org/2017/04/02/522357113/april-come-she-will-with-puzzles
Think of four 4-letter proper names that are all anagrams of each other. 
Two of them are first names — one male and one female. 
The other two are well-known geographical names. What names are these?
'''

from nltk.corpus import names, brown
from collections import defaultdict

def sort_string(s):
    return ''.join(sorted(s))

male_names = [x.lower() for x in names.words("male.txt") if len(x) == 4]
female_names = [x.lower() for x in names.words("female.txt") if len(x) == 4]

male_dict = defaultdict(list)
male_set = set()
for m in male_names:
    male_dict[sort_string(m)].append(m)
    male_set.add(sort_string(m))
    
female_dict = defaultdict(list)
female_set = set()
for f in female_names:
    female_dict[sort_string(f)].append(f)
    female_set.add(sort_string(f))

#%%    
brown_words = frozenset([x.lower() for x in brown.words() if len(x) == 4])
brown_dict = defaultdict(list)
brown_count = defaultdict(int)
for b in brown_words:
    brown_dict[sort_string(b)].append(b)
    brown_count[sort_string(b)] += 1
               
#%%
for s in sorted(male_dict.values()):
    if s in female_set and brown_count[s] >= 1:
        if female_dict[s] != male_dict[s]:
            print male_dict[s], female_dict[s], brown_dict[s]
