#!/usr/bin/env python
"""
NPR 2019-01-27
https://www.npr.org/2019/01/27/688759364/sunday-puzzle-slogan-scramble

Name a vehicle in two words, each with the same number of letters. 
Subtract a letter from each word, and the remaining letters in order will 
spell the first and last names of a famous writer. Who is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
vehicles = nct.wikipedia_category_members('Motor_vehicles_manufactured_in_the_United_States',max_depth=2)
#%%
curated_vehicles = set(x for x in vehicles if x.count(' ') == 1 and len(x.split(' ')[0]) == len(x.split(' ')[1]))

#%%
names = nct.get_famous_names(95)
name_dict = nct.make_sorted_dict(names)
name_keys = frozenset(name_dict.keys())
#%%
for vehicle in curated_vehicles:
    vehicle = vehicle.lower()
    v1,v2 = vehicle.split(' ')
    if v1.isalpha() and v2.isalpha():
        for i in range(len(v1)):
            for j in range(len(v2)):
                sorted_string = nct.sort_string(v1[:i]+v1[i+1:] + v2[:j]+v2[j+1:])
                if sorted_string in name_keys:
                    print(vehicle,name_dict[sorted_string])

