#!/usr/bin/env python
"""
NPR 2018-03-25
https://www.npr.org/2018/03/25/596537250/sunday-puzzle-drop-and-give-me-6

Name a small but well-known U.S. city, followed by its two-letter state 
postal abbreviation. This string of letters, reading from left to right, 
spells two consecutive words that name distinctive characteristics of bunnies. 
What city is it? 
"""
import sys
sys.path.append('..')
import nprcommontools as nct

import requests
from nltk.corpus import wordnet as wn

#%%
cities_states_url = 'https://cdn.rawgit.com/grammakov/USA-cities-and-states/20fa8f6a/us_cities_states_counties.csv'
r = requests.get(cities_states_url)
cities_states_csv = r.content
#%%
cities = dict()
for line in cities_states_csv.split('\n'):
    if '|' in line:
        row = line.split('|')
        cities[nct.alpha_only(row[0].lower()+row[1].lower())] = (row[0],row[1])
#%%
common_words = nct.get_common_words()
#%%
for city_str,city in cities.iteritems():
    for i in range(3,len(city_str)-2):
        w1,w2 = city_str[:i],city_str[i:]
        if w1 in common_words and w2 in common_words:
            print w1,w2,city