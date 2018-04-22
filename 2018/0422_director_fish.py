#!/usr/bin/env python
"""
NPR 2018-04-22
https://www.npr.org/2018/04/22/604475596/sunday-puzzle-lets-play-ball

Take the name of a famous film director. 
Drop the first letter of this person's first name and you'll name a fish. 
Read the last name backward and you'll name another fish. What film director is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
fish = nct.get_category_members('fish')
names = nct.get_famous_names()
#%%
for n in names:
    if n.count(' ') == 1:
        first,last = n.lower().split(' ')
        if last[::-1] in fish and first[1:] in fish:
            print n
