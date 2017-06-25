#!/usr/bin/python
'''
NPR 2017-06-25
http://www.npr.org/2017/06/25/534093188/sunday-puzzle-a-multisyllabic-flip-flop

Take the name KIM KARDASHIAN. 
Rearrange the letters to get the last name of a famous actress 
along with a famous one-named singer. Who are these people?
'''
import sys
sys.path.append('..')
from nprcommontools import get_famous_names,sort_string
#%%
def remove_string(small,big):
    for let in small:
        ix = big.find(let)
        if ix > -1:
            big = big[:ix]+big[ix+1:]
        else:
            return ''
    return sort_string(big)

#%%
names = get_famous_names(98)

one_named_people = set([x.upper() for x in names.keys() if x.count(' ') == 0])
last_name_dict = dict([(sort_string(x.split(' ')[-1].upper()),x) for x in names.keys()])
last_name_set = set(last_name_dict.keys())

#%%
kim = 'KIMKARDASHIAN'
for one in one_named_people:
    r = remove_string(one,kim)
    if r in last_name_set:
        print one, last_name_dict[r]