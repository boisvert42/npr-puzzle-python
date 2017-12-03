#!/usr/bin/python
'''
NPR 2017-12-03
https://www.npr.org/2017/12/03/567605941/sunday-puzzle-the-reverse-is-also-true

Take the singular and plural forms of a particular noun. 
Remove the first two letters of the singular form and you'll name a country. 
Remove one letter from inside the plural form to name another country. 
What words and countries are these?
'''

from nltk.corpus import gazetteers
import json

#%%
# COUNTRIES
COUNTRIES = frozenset([x.lower() for x in gazetteers.words('countries.txt')])

#%%
with open('../plurals.json','rb') as fid:
    plurals = json.load(fid)

for noun in plurals.keys():
    if noun[2:] in COUNTRIES:
        for p in plurals[noun]:
            for i in range(1,len(p)):
                country2 = p[:i]+p[i+1:]
                if country2 in COUNTRIES:
                    print noun,noun[2:],country2
                