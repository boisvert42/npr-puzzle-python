#!/usr/bin/python
'''
NPR 2018-07-08

https://www.npr.org/2018/07/08/626992499/sunday-puzzle-hot-hot-hot

Name part of the human body. Switch the first two letters to get a 
two-word phrase for something that is worrisome. What is it? 
'''
import sys
sys.path.append('..')
import nprcommontools as nct
        
from nltk.corpus import gazetteers

#%%
US_CITIES = set([city.lower() for city in gazetteers.words('uscities.txt')])
US_STATE_ABBREVIATIONS = set([state.lower() for state in
    gazetteers.words('usstateabbrev.txt')])
US_STATES = set([state.lower() for state in gazetteers.words('usstates.txt')])

#%%
for city in US_CITIES:
    city2 = nct.alpha_only(city)
    if len(city2) % 2 == 0:
        continue
    good_flag = True
    while len(city2) > 1:
        abbrev,city2 = city2[:2],city2[2:]
        if abbrev not in US_STATE_ABBREVIATIONS:
            good_flag = False
            break
    if good_flag:
        print city
#%%
for state in US_STATES:
    state2 = nct.alpha_only(state)
    if len(state2) % 2 == 0:
        continue
    good_flag = True
    while len(state2) > 1:
        abbrev,state2 = state2[:2],state2[2:]
        if abbrev not in US_STATE_ABBREVIATIONS:
            good_flag = False
            break
    if good_flag:
        print state