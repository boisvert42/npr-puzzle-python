'''
NPR Puzzle 2016-09-11

www.npr.org/2016/09/11/493408422/its-a-race-to-the-end-of-the-alphabet

Think of a well-known category with exactly seven things in it. 
Alphabetize the things from their ending letters, and the last 
letter alphabetically will be "e." In other words, no thing in 
this category ends in a letter after "e" in the alphabet. 
It's a category and set of seven things that everyone knows. 
What is it?
'''
import sys
sys.path.append('..')
from nprcommontools import get_category_members
from nltk.corpus import wordnet as wn
#%%
def last_letter_alphabetically(l):
    let = ''
    for x in l:
        if x[-1] > let:
            let = x
    return let

#%%
possible_categories = wn.all_lemma_names()
for cat in possible_categories:
    cat_members = get_category_members(cat)
    if len(cat_members) == 7 and last_letter_alphabetically(cat_members) == 'e':
        print cat_members