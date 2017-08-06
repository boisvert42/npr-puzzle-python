#!/usr/bin/env python
"""
NPR 2016-05-15

http://www.npr.org/2016/05/15/477946950/looking-for-common-ground-sometimes-all-it-takes-is-3-letters

Name a creature in nine letters. The name contains a T. 
Drop the T, and the remaining letters can be rearranged 
to spell two related modes of transportation. What are they?
"""
# This doesn't actually give the intended answer but there are some nice alternatives here
import sys
sys.path.append('..')
from nprcommontools import get_category_members, alpha_only

WORD = 'inauguration'

animals = [x for x in get_category_members('animal') if len(alpha_only(x)) == 9 and set(x).issubset(set(WORD))]

print animals