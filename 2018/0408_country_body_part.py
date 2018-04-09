#!/usr/bin/python
'''
NPR 2018-04-08
http://www.npr.org/puzzle

Name part of the human body, insert a speech hesitation, and you'll name a country — what is it?
'''

from nltk.corpus import gazetteers
import nprcommontools as nct

#%%
BODY_PARTS = nct.get_category_members('body_part')

# COUNTRIES
COUNTRIES = frozenset([x.lower() for x in gazetteers.words('countries.txt')])

#%%
for c in COUNTRIES:
    for b in BODY_PARTS:
        if c.startswith(b[0]) and c.endswith(b[-1]):
            for i in range(1,len(b)-1):
                if c.startswith(b[:i]) and c.endswith(b[i:]):
                    print b,c

