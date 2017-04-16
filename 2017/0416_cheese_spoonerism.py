#!/usr/bin/python
'''
NPR 2017-04-16
The name of what famous entertainer -- first and last names --
has a two-word spoonerism meaning "a runny variety of cheese"?
'''
from nltk.corpus import cmudict
cdict = cmudict.dict()
from collections import defaultdict
import sys
sys.path.append('..')
from nprcommontools import get_famous_names, get_category_members

#%%
# Create a "reverse" dictionary (pronunciation to word)
rdict = defaultdict(list)
for k,v in cdict.iteritems():
    for pron in v:
        pron = tuple(pron)
        rdict[pron].append(k)

all_prons = frozenset(rdict.keys())
#%%
def pron_split(p):
    '''
    Extract the first consonant sound from a pronunciation
    Return a tuple of (first sound, the rest)
    '''
    p1 = []
    for i in range(len(p)):
        if any(x.isdigit() for x in p[i]):
            return p1,p[i:]
        else:
            p1.append(p[i])

def spoonerisms(w1,w2):
    '''
    Given two words, return all possible spoonerisms
    '''
    ret = []
    for p1 in cdict.get(w1,[]):
        for p2 in cdict.get(w2,[]):
            p1_1,p1_2 = pron_split(p1)
            p2_1,p2_2 = pron_split(p2)
            s1 = tuple(p2_1 + p1_2)
            s2 = tuple(p1_1 + p2_2)
            if s1 in all_prons and s2 in all_prons and p1_1 != p2_1:
                for w1 in rdict[s1]:
                    for w2 in rdict[s2]:
                        ret.append(w1 + ' ' + w2)
    return ret

#%%
cheeses = [x.lower() for x in get_category_members('cheese') if x.count('_') == 0]
names = frozenset(x.lower() for x in get_famous_names(98).keys() if x.count(' ') == 1)

for name in names:
    n1, n2 = name.split(' ')
    spoon = spoonerisms(n1,n2)
    for s in spoon:
        for c in cheeses:
            if c in s:
                print name,s