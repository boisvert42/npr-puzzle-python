# -*- coding: utf-8 -*-
"""
NPR 2019-03-03
https://www.npr.org/2019/03/03/699735287/sunday-puzzle-in-this-game-a-chance-to-claim-vic-tor-y

Name a popular restaurant chain in two words. 
Its letters can be rearranged to spell some things to eat and some things to drink. 
Both are plural words. What things are these, and what's the chain?
"""
import sys
sys.path.append('..')
import nprcommontools as nct
import json
#%%
# Get a list of restaurants
restaurants = nct.wikipedia_category_members('Restaurant_chains_in_the_United_States',3)
# Two-word restaurants
good_restaurants = set(x for x in restaurants if x.count(' ') == 1)
#%%
# Food and drink are both under the category 'food' in Wordnet
food_and_drink = nct.get_category_members('food')
#%%
# Get plurals of foods
with open(r'../plurals.json','r') as fid:
    plurals1 = json.load(fid)
plurals = set()
for word,pls in plurals1.items():
    if word in food_and_drink:
        for pl in pls:
            plurals.add(pl)
#%%
# All sorted strings consisting of two plurals
plural_dict = dict()
plurals_list = list(plurals)
for i in range(len(plurals_list)):
    for j in range(i+1,len(plurals_list)):
        plural_dict[nct.sort_string(nct.alpha_only(plurals_list[i]+plurals_list[j]))] = (plurals_list[i],plurals_list[j])
#%%
for r in good_restaurants:
    r_sorted = nct.sort_string(nct.alpha_only(r.lower()))
    if r_sorted in plural_dict:
        print(r,plural_dict[r_sorted])
