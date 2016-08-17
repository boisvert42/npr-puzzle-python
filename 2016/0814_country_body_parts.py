'''
NPR Puzzle 2016-08-14

http://www.npr.org/2016/08/14/489898589/the-end-remains-the-same-all-youve-got-to-do-is-find-it

Take the name of a country. Among its letters is the name of part of the human body, 
reading from left to right, although not necessarily consecutively. Cross out these letters. 
The remaining letters in order, reading left to right, will name part of an animal's body. 
What country is it?
'''

import sys
sys.path.append('..')
from nprcommontools import get_category_members, alpha_only
from nltk.corpus import gazetteers

def w1_in_w2(w1,w2):
    '''
    Return leftover letters if all the letters from w1 are in w2
    Return False otherwise
    '''
    for c in w1:
        if c not in w2:
            return False
        else:
            pos = w2.find(c)
            w2 = w2[:pos] + w2[pos+1:]
    return w2

# Country names
countries = set([country.replace(' ','_') for filename in ('isocountries.txt','countries.txt') \
                    for country in gazetteers.words(filename)])

body_parts = get_category_members('body_part')
for country in countries:
    country = alpha_only(country.lower())
    for bp in body_parts:
        bp2 = w1_in_w2(bp,country)
        if bp2 in body_parts:
            print bp,bp2,country
