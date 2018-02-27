#!/usr/bin/env python
"""
NPR 2018-02-25
https://www.npr.org/2018/02/25/588417055/sunday-puzzle-reverse-to-get-ahead

Name a place in the United States that contains a W. 
Drop the W, and you can rearrange the remaining letters to name 
two types of mammals, each in the plural form. 
What place is it, and what are the mammals?
"""
import sys
sys.path.append('..')
import nprcommontools as nct
import requests

from nltk.corpus import gazetteers, wordnet as wn
import json

#%%
# Load plurals
with open('../plurals.json','rb') as fid:
    plurals = json.load(fid)
    
#%%
# Plural mammals
mammals = nct.get_category_members('mammal')
plural_mammals = set()
for m in mammals:
    for p in plurals.get(m.replace('_',' '),[m+'s']):
        plural_mammals.add(p)

#%% 
# Go through pairs of plurals and make the sorted dict
pm_dict = dict()
for m1 in plural_mammals:
    for m2 in plural_mammals:
        sorted_m1_m2 = nct.sort_string(nct.alpha_only(m1+m2).lower())
        pm_dict[sorted_m1_m2] = (m1,m2)

#%%
US_PLACES = set()
url = 'https://cdn.rawgit.com/grammakov/USA-cities-and-states/20fa8f6a/us_cities_states_counties.csv'
r = requests.get(url)
content = r.content
for line in content.split('\n'):
    for w in line.split('|'):
        if 'w' in w.lower():
            US_PLACES.add(w.lower())

#%%
for place in US_PLACES:
    p2 = place.replace('w','',1)
    p2_sorted = nct.sort_string(nct.alpha_only(p2))
    try:
        print pm_dict[p2_sorted], place
    except KeyError:
        pass