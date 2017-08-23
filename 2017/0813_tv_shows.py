#!/usr/bin/env python
"""
NPR 2017-08-13
http://www.npr.org/2017/08/13/543127245/sunday-puzzle-anagrams-across-the-united-states
Name a long-running TV show in two words. Add a C and rearrange the result 
to name another long-running TV show also in two words. What shows are these? 
"""

import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members, alpha_only, sort_string

#%%
tv = wikipedia_category_members('Television_series',max_depth=1)

#%%

tv_dict = dict((sort_string(alpha_only(x.lower())),x) for x in tv)

for x in tv_dict:
    if sort_string(x+'c') in tv_dict:
        print tv_dict[x],tv_dict[sort_string(x+'c')]
