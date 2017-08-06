#!/usr/bin/env python
"""
NPR 2017-08-06

http://www.npr.org/2017/08/06/541834096/sunday-puzzle-a-task-of-8-cities

The name of what 9-letter animal can be spelled from the letters of INAUGURATION?
"""
# This doesn't actually give the intended answer but there are some nice alternatives here
import sys
sys.path.append('..')
from nprcommontools import get_category_members, alpha_only

WORD = 'inauguration'

animals = [x for x in get_category_members('animal') if len(alpha_only(x)) == 9 and set(x).issubset(set(WORD))]

print animals