#!/usr/bin/env python
"""
NPR 2017-10-01

http://www.npr.org/2017/10/01/554491213/sunday-puzzle-put-these-stars-on-the-map

Think of a 4-letter food. Move each letter one space later in the alphabet — 
so A would become B, B would become C, etc. Insert a U somewhere inside the result. 
You'll name a 5-letter food. What foods are these?
"""
import sys
sys.path.append('..')
from nprcommontools import get_category_members, letter_shift
#%%
foods = get_category_members('food')

for food in [_ for _ in foods if len(_) == 4]:
    food_shifted = ''.join(map(lambda x:letter_shift(x,1),food))
    for i in range(5):
        food2 = food_shifted[:i] + 'u' + food_shifted[i:]
        if food2 in foods:
            print food, food2
