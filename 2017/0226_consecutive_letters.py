#!/usr/bin/env python
"""
NPR 2017-02-26
http://www.npr.org/2017/02/26/517289271/if-youve-got-any-compound-interest-solving-this-puzzle-will-surely-pay-off
Take five consecutive letters of the alphabet. 
Write them in left-to-right order. Insert five letters at certain spots. 
These will all go between the first and last given letters. 
The result will be a famous actor — first and last names. Who is it?
"""

import sys
sys.path.append('..')
from nprcommontools import get_famous_names, alpha_only
import re
#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
famous_names = dict((alpha_only(name).lower(),name) for name in get_famous_names(90) if len(alpha_only(name)) == 10)
name_set = frozenset(famous_names.keys())

#%%
for i in range(22):
    re_string = '.*'.join(alphabet[i:i+5])
    regex = re.compile(re_string)
    matches = [m.group(0) for l in name_set for m in [regex.search(l)] if m]
    for m in matches:
        print famous_names[m]