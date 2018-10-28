#!/usr/bin/python
'''
NPR 2018-07-22

https://www.npr.org/2018/07/22/630812232/sunday-puzzle-part-human

Name two parts of the human body. Say them one out loud after the other. 
The result, phonetically, will name something delicious to eat, in 7 letters. What is it? 
'''
import sys
sys.path.append('..')
import nprcommontools as nct
import itertools
from nltk.corpus import cmudict

#%%
# Get cmu dictionary and reverse dictionary
cdict = cmudict.dict()
reverse_dict = dict()
for word,prons in cdict.iteritems():
    for p in prons:
        for i in range(len(p)):
            p[i] = nct.alpha_only(p[i])
        val = reverse_dict.get(tuple(p),[])
        val.append(word)
        reverse_dict[tuple(p)] = val

#%%
# Get set of body parts
body_parts = set(x for x in nct.get_category_members('body_part') if len(x) == 4)

#%%
for b1,b2 in itertools.product(body_parts,body_parts):
    for p1,p2 in itertools.product(cdict.get(b1,[]),cdict.get(b2,[])):
        new_pron = p1+p2
        for i in range(len(new_pron)):
            new_pron[i] = nct.alpha_only(new_pron[i])
        new_pron = tuple(new_pron)
        new_words = reverse_dict.get(new_pron,[])
        for new_word in new_words:
            if len(new_word) == 7:
                print b1,b2,new_word