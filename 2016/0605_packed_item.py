'''
NPR Puzzle 2016-06-05

http://www.npr.org/2016/06/05/480617338/to-solve-this-puzzle-lets-do-some-math-5-plus-2-equals

Name a famous actor — seven-letter first name, 
four-letter last name. Take four consecutive letters 
from the first name and three consecutive letters from 
the last name. These seven letters, in order from left 
to right, will name something that's often packed 
nowadays when taking a trip. What is it?
'''
import sys
sys.path.append('..')
from nprcommontools import get_famous_names, get_category_members
import re

#%%
objects = frozenset([x for x in get_category_members('physical_object') \
    if x == x.lower() and len(x) == 7 and x.isalpha()])

#%%
all_names = get_famous_names()
names = [k.lower() for k in all_names.keys() if re.match('^\w{7} \w{4}$',k)]

#%%
for name in names:
    first_name, last_name = name.split(' ')
    for i in range(4):
        for j in range(2):
            s1 = first_name[i:i+4]
            s2 = last_name[j:j+3]
            if s1+s2 in objects:
                print name, s1+s2