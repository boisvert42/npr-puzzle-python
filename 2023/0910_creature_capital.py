# -*- coding: utf-8 -*-
"""
https://www.npr.org/2023/09/10/1198507860/sunday-puzzle-switch-it-out

Name a creature that has a world capital in its name. 
Replace the capital with another creature and you'll 
get another world capital. What is it?
"""

import nprcommontools as nct

from nltk.corpus import wordnet as wn, gazetteers

#%% Get a list of world capitals
COUNTRIES = frozenset(gazetteers.words('countries.txt'))

# State and world capitals
world_capitals = set()
for s in wn.all_synsets():
    d = s.definition()
    if 'capital' in d:
        for country in COUNTRIES:
            if country in d:
                for l in s.lemma_names():
                    if l[0] == l[0].upper() and 'capital' not in l:
                        world_capitals.add(l.lower())
                        
#%% Get a list of "creatures"
creatures = nct.get_category_members('creature')

for creature in creatures:
    for capital in world_capitals:
        if capital in creature:
            for creature2 in creatures:
                word2 = creature.replace(capital, creature2)
                if word2 in world_capitals:
                    print(creature, capital, word2)

