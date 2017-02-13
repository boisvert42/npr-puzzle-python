#!/usr/bin/python
'''
NPR 2017-02-12
'''
import sys
sys.path.append('..')
from npr_common_tools import get_category_members

objects = get_category_members('object')
for word in objects:
    plural = word + 's'
    if len(plural) >= 6:
        new_word = plural[:4] + plural[5] + plural[4] + plural[6:]
        new_word = new_word[::-1]
        for i in range(1,len(new_word)-1):
            if new_word[:i] in objects and new_word[i:] in objects:
                print plural, new_word[:i], new_word[i:]
