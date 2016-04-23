#!/usr/bin/env python
'''
NPR 2015-11-22

http://www.npr.org/2015/11/22/456942541/high-level-puzzlers-will-have-figured-out-this-headline-by-now

This week's Thanksgiving challenge comes from listener Dan Pitt of Palo Alto, Calif. 
It's not very hard. The following three Thanksgiving dishes have something 
very unusual in common:

Spit-roast turkey
Cornbread stuffing
Boiled squash

What is it they have in common, and can you name one other thing 
that might be served at Thanksgiving dinner that has the same property?
'''
# Once we realize that they all have a,e,i,o,u only once ...
import sys
sys.path.append('..')
from nprcommontools import get_category_members

foods = get_category_members('food')
for x in foods:
    if x.count('a') == 1 and x.count('e') == 1 and x.count('i') == 1 and x.count('o') == 1 and x.count('u') == 1:
        print x
