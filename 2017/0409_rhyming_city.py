#!/usr/bin/python
'''
NPR 2017-04-09
Name a well-known U.S. city in two words.  Replace each of these words with a 
word that rhymes with it, and you'll name a large sea creature in two words.
What is it?
'''
import sys
sys.path.append('..')
from nprcommontools import get_category_members
import rhyme
from nltk.corpus import gazetteers
#%%
ANIMALS = frozenset([x for x in get_category_members('animal') if x.count('_') == 1])
USCITIES = set([x.lower() for x in gazetteers.words('uscities.txt') if x.count(' ') == 1])
# Cheating but honestly why wasn't this in there?
USCITIES.add('santa fe')

#%%
for city in USCITIES:
    c1,c2 = city.split(' ')
    c1_rhymes = rhyme.all_rhymes(c1)
    c2_rhymes = rhyme.all_rhymes(c2)
    for a1 in c1_rhymes:
        for a2 in c2_rhymes:
            if a1 + '_' + a2 in ANIMALS:
                print city, a1, a2
