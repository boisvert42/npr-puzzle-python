#!/usr/bin/env python
"""
NPR 2018-04-15
https://www.npr.org/2018/04/15/602535575/sunday-puzzle-easy-as-pie

The letters of SWITZERLAND can be rearranged to spell LIZARD and NEWTS — 
LIZARD being the singular name of an animal, and NEWTS a plural. 
Name another country with this same property. 
That is, name another country whose letters can be rearranged to spell 
two animals — one singular and one plural. It's a major country. What country is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct
from nltk.corpus import gazetteers
import json

#%%
countries = set([country.lower() for filename in ('isocountries.txt','countries.txt')
  for country in gazetteers.words(filename)])

country_dict = nct.make_sorted_dict(countries)

animals = nct.get_category_members('animal')
with open('../plurals.json','rb') as fid:
    plural_dict = json.load(fid)

plural_animals = set()
for x in animals:
    try:
        p = plural_dict[x]
        for p1 in p:
            plural_animals.add(p1)
    except KeyError:
        pass

#%%
for a in animals:
    for p in plural_animals:
        if country_dict.get(nct.sort_string(a+p),None) is not None:
            print a,p,country_dict.get(nct.sort_string(a+p),None)