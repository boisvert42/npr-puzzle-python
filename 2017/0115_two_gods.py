#!/usr/bin/env python
"""
NPR 2017-01-15
http://www.npr.org/puzzle
Take the first and last names of a famous comedian.
The first three letters of the first name and the
first letter of the last name, in order, spell the
name of a god in mythology.  The fourth letter of
the first name and the second through fourth letters
of the last name, in order, spell another god.  Who's
the comedian, and what gods are these?

"""

import sys
sys.path.append('..')
from nprcommontools import get_famous_names
from nltk.corpus import wordnet as wn
#%%
# Get a set of gods
gods = frozenset([lemma_name.lower() for s in wn.all_synsets() \
    for lemma_name in s.lemma_names() \
    if 'mythology' in s.definition() and 'god' in s.definition()
    ])

#%%
# Loop through names to find a match
for name in get_famous_names():
    try:
        split_name = name.lower().split(' ')
        first_name, last_name = split_name[0], split_name[-1]
        god1 = first_name[:3]+last_name[0]
        god2 = first_name[3] + last_name[1:4]
        if god1 in gods and god2 in gods:
            print name, god1, god2
    except IndexError:
        pass