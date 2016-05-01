#!/usr/bin/env python
'''
NPR 2015-11-29

http://www.npr.org/2015/11/29/457591424/between-alphabetizing-and-best-guesses-can-you-find-this-weeks-answers

Take the name of a well-known actress — four letters in the first name, 
nine letters in the last. Insert a letter between the second and 
third letters of the first name. Remove the last two letters of the 
last name. The result is a two-word phrase that means "freedom."
'''

import sys
sys.path.append('..')
from nprcommontools import get_famous_names

from nltk.corpus import wordnet as wn
import re

names = [x for x in get_famous_names() if re.match(r'^\w{4} \w{9}$',x)]

phrases = dict([(x.replace('_',''),x) for x in wn.all_lemma_names() if len(x) == 13 and x.count('_') == 1 and x == x.lower()])
phrase_set = frozenset(phrases.keys())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for name in names:
    name2 = name.lower()
    first_name, last_name = name2.split(' ')
    for letter in alphabet:
        test = first_name[:2] + letter + first_name[2:] + last_name[:-2]
        if test in phrase_set:
            print name, phrases[test]