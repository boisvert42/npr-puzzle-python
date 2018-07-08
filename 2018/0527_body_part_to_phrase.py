#!/usr/bin/python
'''
NPR 2018-05-27

https://www.npr.org/2018/05/27/614535615/sunday-puzzle-yo

Name part of the human body. Switch the first two letters to get a 
two-word phrase for something that is worrisome. What is it? 
'''
import sys
sys.path.append('..')
import nprcommontools as nct
        
from nltk.corpus import wordnet as wn

#%%
# Get set of body parts
body_parts = nct.get_category_members('body_part')
body_part_dict = dict((nct.alpha_only(b),b) for b in body_parts)

#%%
# Two-word phrases
phrases = [x for x in wn.all_lemma_names() if x.count('_') == 1]
phrase_dict = dict((nct.alpha_only(p),p) for p in phrases)

#%%
for ab,b in body_part_dict.iteritems():
    p1 = ab[1] + ab[0] + ab[2:]
    if p1 in phrase_dict:
        print b,phrase_dict[p1]
