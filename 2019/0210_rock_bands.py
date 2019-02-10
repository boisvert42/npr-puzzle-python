# -*- coding: utf-8 -*-
"""
NPR 2019-02-10
https://www.npr.org/2019/02/10/692431826/sunday-puzzle-3rd-o

Name a well-known rock band in three words. 
Change the first and third letters to the first and third letters of the 
alphabet — that is, A and C. You can rearrange the result to name another 
famous rock band in three words. What is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
rock_bands = nct.wikipedia_category_members('Rock_music_groups_by_genre',2)
#%%
rb_dict = nct.make_sorted_dict(rock_bands)
for r in rock_bands:
    if r.count(' ') == 2:
        r1 = nct.alpha_only(r.lower())
        r2 = 'a' + r1[1] + 'c' + r1[3:]
        try:
            r3 = rb_dict[nct.sort_string(r2)][0]
            if r3.count(' ') == 2 and r3 != r:
                print(r,r3)
        except:
            pass