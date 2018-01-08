#!/usr/bin/env python
"""
NPR 2018-01-07
https://www.npr.org/2018/01/07/575920963/sunday-puzzle-whats-the-fourth-word

Take the first and last names of a journalist well-known to NPR listeners. 
Remove the first letter of the last name. 
The remaining letters can be rearranged to spell two modes of transport. 
And here's a hint: The modes of transport have the same number of wheels. 
Who is the journalist, and what are the modes of transport?
"""
#%%
import sys
sys.path.append('..')

import nprcommontools as nct

modes_of_transport = nct.get_category_members('transport')
transport_dict = dict()
transport_set = set()
for m1 in modes_of_transport:
    for m2 in modes_of_transport:
        if m1 < m2:
            m = nct.sort_string(nct.alpha_only(m1+m2).lower())
            transport_set.add(m)
            transport_dict[m] = transport_dict.get(m,[]) + [(m1,m2)]
#%%
#names = nct.get_famous_names(90)
names = nct.wikipedia_category_members('NPR_personalities')
for name in names:
    if name.count(' ') == 1:
        n2 = name.split(' ')[0] + name.split(' ')[1][1:]
        n2 = nct.sort_string(nct.alpha_only(n2.lower()))
        if n2 in transport_set:
            print name, transport_dict[n2]
        