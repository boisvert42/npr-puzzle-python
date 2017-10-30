#!/usr/bin/python
'''
NPR Puzzle 2017-10-29

http://www.npr.org/2017/10/29/560492280/sunday-puzzle-it-doesnt-take-a-know-it-all-to-play-this-game

Name a well-known nationality. Drop a letter, and the remaining letters 
in order will name a metal — one of the elements on the periodic table. What is it?
'''

import sys
sys.path.append('..')
from nprcommontools import get_category_members

def w1_in_w2(w1,w2):
    '''
    Return True if all the letters from w1 are in w2 in order
    Return False otherwise
    '''
    for c in w1:
        if c not in w2:
            return False
        else:
            pos = w2.find(c)
            w2 = w2[pos+1:]
    return True

#%%
elements = get_category_members('chemical_elements')
nationalities = [x.lower() for x in get_category_members('inhabitant') if x[0] == x[0].upper()]

for n in nationalities:
    for e in elements:
        if w1_in_w2(e,n):
            print e,n
