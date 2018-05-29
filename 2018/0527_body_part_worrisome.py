#!/usr/bin/python
"""
NPR 2018-05-27
https://www.npr.org/2018/05/27/614535615/sunday-puzzle-yo

Name part of the human body. Switch the first two letters to get 
a two-word phrase for something that is worrisome. What is it? 
"""

import sys
sys.path.append('..')
import nprcommontools as nct

COMMON_WORDS = nct.get_common_words()

#%%
body_parts = nct.get_category_members('body_part')
body_part_dict = dict((nct.alpha_only(b),b) for b in body_parts if len(b) >= 6)

#%%
for b1,b in body_part_dict.iteritems():
    b2 = b1[1]+b1[0] + b1[2:]
    # do an inefficient loop through this
    for i in range(2,len(b2)-1):
        w1,w2 = b2[:i],b2[i:]
        if w1 in COMMON_WORDS and w2 in COMMON_WORDS:
            print b,w1,w2
