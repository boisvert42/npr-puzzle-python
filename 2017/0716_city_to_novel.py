#!/usr/bin/python
'''
NPR 2017-07-16
http://www.npr.org/2017/07/16/537225382/sunday-puzzle-wehn-wrods-get-rearearngd

Name a U.S. city and its state — 12 letters altogether. 
Change two letters in the state's name. 
The result will be the two-word title of a classic novel. What is it?
'''

from nltk.corpus import gazetteers
import re

us_states = frozenset(gazetteers.words('usstates.txt'))

#%%
# via http://norvig.com/spell-correct.html
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    return set(replaces)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

#%%
# Need the ranked Wikipedia entries from http://crosswordnexus.com/wiki
# Read in city, state combinations and also anything else that is 12 letters long

cities = set()
entries = dict()
with open(r'RankedWiki.txt','rb') as fid:
    for line in fid.readlines():
        line = line.strip()
        word,score = line.split('@')
        if int(score) >= 95:
            alpha_only = re.sub('[^A-Za-z]+','',word).lower()
            if len(alpha_only) == 12:
                # Check to see if this is a city,state
                try:
                    city,state = word.split(', ')
                    if state in us_states:
                        cities.add(word)
                except ValueError:
                    pass
                if word not in cities:
                    entries[alpha_only] = word
                    
entries_keys = frozenset(entries.keys())
                
#%%
for place in cities:
    city2 = place.lower()
    city,state = place.split(', ')
    city = re.sub('[^A-Za-z]+','',city).lower()
    state = re.sub('[^A-Za-z]+','',state).lower()
    for e in edits2(state):
        if city+e in entries_keys:
            print place,entries[city+e]
