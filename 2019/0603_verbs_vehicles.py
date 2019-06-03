#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NPR 2019-06-02
https://www.npr.org/2019/06/02/728600551/sunday-puzzle-lets-go-toe-to-toe?utm_medium=RSS&utm_campaign=sundaypuzzle

Think of a verb in its present and past tense forms. 
Drop the first letter of each word. 
The result will name two vehicles. What are they?
"""

import requests
import sys
sys.path.append('..')
import nprcommontools as nct

# URL with verb forms
URL = 'https://cdn.jsdelivr.net/gh/kulakowka/english-verbs-conjugation@master/src/services/ConjugationService/verbs.json'
r = requests.get(URL)
j = r.json()

VEHICLES = frozenset(nct.get_category_members('vehicle'))

#%%
for d in j:
    verb = d[0]
    past = d[1]
    if past is not None:
        v1 = verb[1:]
        p1 = past[1:]
        if v1 in VEHICLES and p1 in VEHICLES:
            print(verb, past, v1, p1)
