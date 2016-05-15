#!/usr/bin/env python
"""
NPR 2016-05-15

http://www.npr.org/2016/05/15/477946950/looking-for-common-ground-sometimes-all-it-takes-is-3-letters

Name a creature in nine letters. The name contains a T. 
Drop the T, and the remaining letters can be rearranged 
to spell two related modes of transportation. What are they?
"""
# This doesn't actually give the intended answer but there are some nice alternatives here
import sys
sys.path.append('..')
from nprcommontools import get_category_members, alpha_only, sort_string

animals = [x for x in get_category_members('animal') if len(alpha_only(x)) == 9 and 't' in x and x == x.lower()]
animals_no_t = dict([(sort_string(alpha_only(x).replace('t','',1)),x) for x in animals])

transport = [alpha_only(x) for x in get_category_members('transport') if len(alpha_only(x)) <= 7]

for i in range(len(transport)):
    for j in range(i,len(transport)):
        t1 = transport[i]; t2 = transport[j]
        try:
            animal = animals_no_t[sort_string(t1+t2)]
            print t1,t2,animal
        except KeyError:
            pass