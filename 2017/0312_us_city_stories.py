#!/usr/bin/env python
"""
NPR 2017-03-12
http://www.npr.org/2017/03/12/519877647/find-the-words-with-letters-in-common-in-these-categories
Name a well-known city in the U.S. Two words. The second word rhymes with a word meaning 
"certain stories" — and the first word rhymes with something found in those stories. What city is it?
"""

import sys
sys.path.append('..')
from nprcommontools import alpha_only, get_category_members
import rhyme
import json
from nltk.corpus import gazetteers
#%%
with open('../plurals.json','rb') as fid:
    plurals = json.load(fid)

#%%
# U.S. cities from gazetteers
US_CITIES = set([city.lower() for city in gazetteers.words('uscities.txt') if city.count(' ') == 1])
# cheating
US_CITIES.add('coral gables')

#%%
# Words that mean "kind of story"
stories = get_category_members('story')
story_plurals = set()
for x in stories:
    try:
        for y in plurals[x]:
            story_plurals.add(y)
    except KeyError:
        pass
    
for city in US_CITIES:
    word1, word2 = city.split(' ')
    rhymes = [_ for _ in story_plurals if rhyme.does_rhyme(_,word2)]
    if rhymes:
        print city, rhymes