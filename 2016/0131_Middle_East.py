#!/usr/bin/env python
"""
NPR 2016-01-31

http://www.npr.org/2016/01/31/464999462/stuck-in-the-middle-with-u-or-a-or-b

Take the name of a country and a well-known city in the Middle East — 12 letters in all. 
Rearrange these letters to name another country and another well-known city in the Middle East. 
What places are these?
"""
import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members

from nltk.corpus import wordnet as wn
from collections import defaultdict
import re

# Middle eastern countries
middle_east_countries = wikipedia_category_members('Middle_Eastern_countries')
#%%
# Middle eastern cities
cities = set()
for synset in wn.all_synsets():
    if 'city' in synset.definition() or 'capital' in synset.definition():
        for country in middle_east_countries:
            if country in synset.definition():
                for lemma_name in synset.lemma_names():
                    if lemma_name[0] == lemma_name[0].upper():
                        cities.add(re.sub(r'[^A-Za-z_]+','',lemma_name))

# There's a "Bursa" and "Brusa" in cities -- remove one
cities.remove('Brusa')
                        
#%%
match_dict = defaultdict(list)
for country in middle_east_countries:
    for city in cities:
        country2 = country.lower(); country2 = re.sub(r'[^a-z]+','',country2)
        city2 = city.lower(); city2 = re.sub(r'[^a-z]+','',city2)
        match_dict[''.join(sorted(country2+city2))].append((country,city))
        
for v in match_dict.itervalues():
    if len(v) >= 2:
        print v
        