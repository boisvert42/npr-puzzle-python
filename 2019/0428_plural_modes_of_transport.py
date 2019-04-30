#!/usr/bin/python
'''
NPR 2019-04-28

https://www.npr.org/2019/04/28/717915342/sunday-puzzle-fame-game

Think of a familiar three-word phrase with "and" in the middle ("___ and ___"). 
Move the first letter of the third word to the start of the first word, and you'll 
form two means of transportation. What are they?
'''
import sys
sys.path.append('..')
import nprcommontools as nct
import json

from nltk.corpus import wordnet as wn

with open('../plurals.json','r') as fid:
    plurals = json.load(fid)

modes_of_transport = nct.get_category_members('transport')
plural_modes_of_transport = set()
for m in modes_of_transport:
    for p in plurals.get(m,[]):
        plural_modes_of_transport.add(p)
        
and_phrases = [x for x in wn.all_lemma_names() if '_and_' in x and x.count('_') == 2]

for phrase in and_phrases:
    w1,w2,w3 = phrase.split('_')
    p1 = w3[0] + w1
    p2 = w3[1:]
    if p1 in plural_modes_of_transport and p2 in plural_modes_of_transport:
        print(phrase, p1, p2)
