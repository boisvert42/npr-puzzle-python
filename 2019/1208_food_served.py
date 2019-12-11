#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://www.npr.org/2019/12/08/785832131/sunday-puzzle-bs-and-l-s

Name a food in two words — a total of 11 letters. 
Some of these letters appear more than once. 
The food has seven different letters in its name. 
You can rearrange these seven letters to identify the form 
in which this food is typically served. What food is it?
"""

#%%
import sys
sys.path.append('..')
from nltk.corpus import wordnet as wn
import nprcommontools as nct

foods = nct.get_category_members('food')
foods_11 = [x for x in foods if len(nct.alpha_only(x)) == 11 and len(set(nct.alpha_only(x))) == 7 and x.count('_') == 1]

#%%
all_words_7 = [x for x in wn.all_lemma_names() if len(nct.alpha_only(x)) == 7 and len(set(nct.alpha_only(x))) == 7]
all_words_7_dict = nct.make_sorted_dict(all_words_7)

#%%
for x in foods_11:
    y = nct.sort_string(set(nct.alpha_only(x)))
    if y in all_words_7_dict:
        print(x, all_words_7_dict[y])
