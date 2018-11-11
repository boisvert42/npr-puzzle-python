#!/usr/bin/python
'''
NPR 2018-11-11

https://www.npr.org/2018/11/11/666376065/sunday-puzzle-lets-get-phonetical

Think of a familiar four-word phrase that means "to be last." 
Together the first two words are a synonym for the last word. What phrase is it?
'''
import sys
sys.path.append('..')
import nprcommontools as nct

from nltk.corpus import wordnet as wn
#%%
# This doesn't actually give the answer.
four_word_phrases = [x for x in wn.all_lemma_names() if x.count('_') == 3]
for p in four_word_phrases:
    words = p.split('_')
    first_two_words = words[0] + '_' + words[1]
    if first_two_words in nct.get_synonyms(words[-1]):
        print(p)