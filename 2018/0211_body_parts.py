#!/usr/bin/env python
"""
NPR 2018-02-11
https://www.npr.org/2018/02/11/584000987/sunday-puzzle-put-your-back-into-it

Name part of the human body in six letters. 
Add an R and rearrange the result to name a part of the body in seven letters. 
What is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
body_parts = [w for w in nct.get_category_members('body_part') if len(w) in (6,7)]
d = nct.make_sorted_dict(body_parts)

for b1 in body_parts:
    b2_sorted = nct.sort_string(b1+'r')
    if b2_sorted in d.keys():
        print b1, d[b2_sorted]