#!/usr/bin/python
'''
NPR 2019-05-12

https://www.npr.org/2019/05/12/722484920/sunday-puzzle-clues-come-in-2s

Think of a 6-letter conveyance on wheels. Drop the first letter. 
Add a new letter at the end. The result will be another 6-letter 
conveyance on wheels. What conveyances are these?
'''
import sys
sys.path.append('..')
import nprcommontools as nct

modes_of_transport = [x for x in nct.get_category_members('transport') if x.isalpha() and len(x) == 6]

for conveyance in modes_of_transport:
    c2 = [x for x in modes_of_transport if x.startswith(conveyance[1:])]
    if c2:
        print(conveyance, c2)
