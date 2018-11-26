#!/usr/bin/python
'''
NPR 2018-11-11

https://www.npr.org/2018/11/25/670596165/sunday-puzzle-the-big-mo

Think of a well-known food brand. Add the letters W-O-W. 
Then rearrange the result to name another well-known food brand. What is it?
'''
import sys
sys.path.append('..')
import nprcommontools as nct

from nltk.corpus import wordnet as wn
#%%
food_brands = nct.wikipedia_category_members('Food_product_brands',max_depth=3)

#%%
food_dict = nct.make_sorted_dict(food_brands)
food_keys = set(food_dict.keys())
for f1 in food_dict:
    if f1.count('w') >= 2 and f1.count('o') >= 1:
        f2 = f1.replace('w','',2)
        f2 = f2.replace('o','',1)
        f2 = ''.join(sorted(f2))
        if f2 in food_keys:
            print(food_dict[f1],food_dict[f2])

