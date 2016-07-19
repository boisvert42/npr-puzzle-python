'''
NPR Puzzle 2016-07-03

http://www.npr.org/2016/07/17/486308247/better-get-revved-up-for-a-puzzle-stuffed-with-vs-and-es

Name a prominent American politician — first and last names, 11 letters total. 
Rearrange these letters, and you'll get a country plus the former name of another country. 
Who's the politician, and what countries are these?
'''

import sys
sys.path.append('..')
from nprcommontools import get_famous_names, alpha_only, sort_string
from nltk.corpus import wordnet as wn, gazetteers

#%%
# Country names
countries_current = set([country.replace(' ','_') for filename in ('isocountries.txt','countries.txt') \
                    for country in gazetteers.words(filename)])
# Grow this list with Wordnet
# This adds old names of countries (and a ton of other stuff)
countries = set()
for c in countries_current:
    s = wn.synsets(c)
    for synset in s:
        for l in synset.lemma_names():
            if l[0] == l[0].upper() and len(l) <= 10:
                countries.add(l)
                
countries_old = countries.difference(countries_current)
countries_current = set(_x for _x in countries_current if len(_x) <= 10)
                
#%%
names = frozenset(get_famous_names(90).keys())
name_dict = dict([(sort_string(alpha_only(name.lower())), name) for name in names if len(alpha_only(name)) == 11])
sorted_names = frozenset(name_dict.keys())

for c1 in countries_current:
    for c2 in countries_old:
        c1c2 = sort_string(alpha_only((c1+c2).lower()))
        if c1c2 in sorted_names:
            print name_dict[c1c2], c1, c2
