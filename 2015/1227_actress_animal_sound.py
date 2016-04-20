#!/usr/bin/env python
'''
NPR 2015-12-27

http://www.npr.org/2015/12/27/461108931/should-old-acquaintance-be-forgot-at-least-recall-these-headline-grabbers

Name a famous actress who has four letters in her first name 
and four letters in her last name. Add one letter, and rearrange 
the result to name an animal and the sound this animal makes. 
Who is the actress, what is the animal and what is the sound 
that the animal makes?
'''

import sys
sys.path.append('..')
from nprcommontools import get_category_members, get_famous_names

from nltk.corpus import wordnet as wn
import re
from collections import defaultdict

# Animals
animals = get_category_members(wn.synset('animal.n.01'))
# Remove any scientific names
animals = set([x for x in animals if x == x.lower()])

# Animal sounds -- from "utter" and "cry"
synsets = [wn.synset('cry.n.05'),wn.synset('utter.v.02')]
animal_sounds = set()
for s in synsets:
    animal_sounds = animal_sounds.union(get_category_members(s))
    
#%%
# Make a dictionary for easy anagramming
anagram_dict = defaultdict(list)
for animal in animals:
    for sound in animal_sounds:
        key = ''.join(sorted(animal+sound))
        key = re.sub(r'[^a-z]+','',key)
        anagram_dict[key].append((animal,sound))
all_keys = frozenset(anagram_dict.keys())
        
#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
names = get_famous_names()
for name in names:
    if name.count(' ') == 1:
        first_name, last_name = name.lower().split(' ')
        if len(first_name) == 4 and len(last_name) == 4 and first_name.isalpha() and last_name.isalpha():
            for letter in alphabet:            
                key = ''.join(sorted(first_name+last_name+letter))            
                if key in all_keys:
                    print name,anagram_dict[key]