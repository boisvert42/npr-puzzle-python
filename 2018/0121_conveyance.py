#!/usr/bin/env python
"""
NPR 2018-01-21
https://www.npr.org/2018/01/21/579110492/sunday-puzzle-it-takes-two

Take the name of a conveyance in seven letters. 
Drop the middle letter, and the remaining letters can be rearranged to name 
the place where such a conveyance is often used. What is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
#words = nct.get_common_words('brown')
words = nct.get_category_members('physical_entity')
word_dict = nct.make_sorted_dict(words)
sorted_set = frozenset(word_dict.keys())
#%%
conveyances = [x for x in nct.get_category_members('conveyance') if x.isalpha() and len(x) == 7]
for conv in conveyances:
    sorted_conv = nct.sort_string(conv[:3]+conv[4:])
    if sorted_conv in sorted_set:
        print conv, word_dict[sorted_conv]
