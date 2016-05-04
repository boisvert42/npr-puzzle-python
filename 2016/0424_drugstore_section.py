'''
NPR Puzzle 2016-04-24

http://www.npr.org/2016/04/24/475299329/finish-this-puzzle-and-youll-be-just-like-overachievers-you-both-exceed

Name a famous singer -- first and last names. 
The last four letters of the first name spelled 
backward plus the first four letters of the last name 
spelled forward, read together, in order, name a 
section of products in a drugstore. What is it?
'''
import sys
sys.path.append('..')
from nprcommontools import get_famous_names

from nltk.corpus import wordnet as wn
import re
#%%
lemmas = wn.all_lemma_names()
lemma_dict = dict([(re.sub(r'[^a-z]+','',x),x) for x in lemmas if x == x.lower()])
names = get_famous_names()
for name in names.iterkeys():
    if name.count(' ') == 1:
        first_name, last_name = name.lower().split(' ')
        if len(first_name) >= 4 and len(last_name) >= 4:
            word = first_name[-1:-5:-1] + last_name[:4]
            try:
                print lemma_dict[word], name
            except KeyError:
                pass
