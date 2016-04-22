#!/usr/bin/env python
'''
NPR 2015-12-13

http://www.npr.org/2015/12/13/459493157/when-fbi-gets-involved-in-puzzles-clues-are-just-the-half-of-it

Name a well-known character of TV, movies and comics. Two words. 
Replace the 8th, 9th, and 10th letters with an S. 
Then rearrange the result to name a well-known actor who played 
this character on film. First and last names. Who is it?
'''

import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members, get_famous_names, sort_string

comics_categories = ('DC_Comics_superheroes','Marvel_Comics_superheroes')
heroes = set()
for cc in comics_categories:
    heroes = heroes.union(wikipedia_category_members(cc))
    
hero_sorted = dict()
for hero in [x for x in heroes if len(x) >= 10 and x.count(' ') == 1]:
    hero_nospace = hero.lower().replace(' ','')
    hero_replace = hero_nospace[:7] + 's' + hero_nospace[10:]
    hero_sorted[sort_string(hero_replace)] = hero

names = get_famous_names()
for name in names:
    try:
        print hero_sorted[sort_string(name.lower().replace(' ',''))], name
    except KeyError:
        pass
