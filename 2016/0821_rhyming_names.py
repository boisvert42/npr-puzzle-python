'''
NPR Puzzle 2016-08-21

http://www.npr.org/2016/08/21/490647499/name-that-celebrity-all-you-have-to-do-is-rhyme

Name a famous person with the initials B.S. and another famous person with the initials G.M.
 — whose first and last names, respectively, rhyme with each other. 
One of the names has one syllable and one has two syllables. Who are these famous people?
'''

import sys
sys.path.append('..')
from nprcommontools import get_famous_names
import rhyme

names = get_famous_names(minscore=98)

# Only names with the relevant initials
bs_names = []; gm_names = []
for name in names.iterkeys():
    try:    
        first,last = name.split(' ')
    except ValueError:
        continue
    if first.startswith('G') and last.startswith('M'):
        gm_names.append(name.lower())
    elif first.startswith('B') and last.startswith('S'):
        bs_names.append(name.lower())
        
for n1 in bs_names:
    for n2 in gm_names:
        try:
            b, s = n1.split(' ')
            g, m = n2.split(' ')
            if rhyme.does_rhyme(b,g) and rhyme.does_rhyme(s,m):
                print n1, n2
        except ValueError:
            pass