#!/usr/bin/python
'''
NPR 2017-11-12
https://www.npr.org/2017/11/12/563367879/sunday-puzzle-move-around-to-find-new-meaning

Take the name of a U.S. state capital. Immediately to the right of it write the name 
of a world capital. If you have the right ones, the name of a U.S. state will be 
embedded in consecutive letters within that letter string. What three places are these?
'''

from nltk.corpus import wordnet as wn, gazetteers

#%%
# US states
US_STATES = frozenset(gazetteers.words('usstates.txt'))
US_STATES_LOWER = frozenset(x.lower().replace(' ','') for x in US_STATES)

# COUNTRIES
COUNTRIES = frozenset(gazetteers.words('countries.txt'))

# State and world capitals
state_capitals = set(); world_capitals = set()
for s in wn.all_synsets():
    d = s.definition()
    if 'capital' in d:
        for state in US_STATES:
            if state in d:
                for l in s.lemma_names():
                    if l[0] == l[0].upper() and 'capital' not in l:
                        state_capitals.add(l.lower())
        for country in COUNTRIES:
            if country in d:
                for l in s.lemma_names():
                    if l[0] == l[0].upper() and 'capital' not in l:
                        world_capitals.add(l.lower())

#%%
for c in state_capitals:
    for w in world_capitals:
      for s in US_STATES_LOWER:
          if s in c+w and s not in c and s not in w:
              print c,w,s
