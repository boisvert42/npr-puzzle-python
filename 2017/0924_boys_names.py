#!/usr/bin/env python
"""
NPR 2017-09-24

http://www.npr.org/2017/09/24/553147004/sunday-puzzle-what-s-in-a-name

Think of a familiar 6-letter boy's name starting with a vowel. 
Change the first letter to a consonant to get another familiar boy's name. 
Then change the first letter to another consonant to get another familiar boy's name. 
What names are these?
"""

from nltk.corpus import names
from collections import defaultdict

#%%
name_dict = defaultdict(set)
for name in names.words('male.txt'):
    name_dict[name[1:]].add(name[0])
    
#%%
for k,v in name_dict.iteritems():
    if len(v) >= 3 and len(k) == 5 and set('AEIOU').intersection(v):
        for letter in v:
            print letter+k, 
        print