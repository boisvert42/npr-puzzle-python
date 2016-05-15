'''
NPR Puzzle 2016-05-08

http://www.npr.org/2016/05/08/477092627/want-to-find-a-synonym-better-get-to-shufflin

Name something in 11 letters that's a common household item. 
You can rearrange the first six letters to form a 
synonym of a word spelled by the middle three letters. 
What is the item, and what are the words?
'''
import sys
sys.path.append('..')
from nprcommontools import get_synonyms, sort_string, get_hypernyms
from nltk.corpus import wordnet as wn, brown
import re
from collections import defaultdict
#%%
words = [x.lower() for x in brown.words() if len(x) in (3,6)]
#%%
eleven = set()
six = defaultdict(list)
three = set()
sorted_six = set()
for word in wn.all_lemma_names():
    alphaword = re.sub(r'[^A-Za-z]+','',word)
    if len(alphaword) == 11:
        if 'physical_object' in get_hypernyms(word):
            eleven.add(word)
    elif len(alphaword) == 6 and alphaword in words:
        six[sort_string(alphaword)].append(word)
        sorted_six.add(sort_string(alphaword))
    elif len(alphaword) == 3 and alphaword in words:
        three.add(alphaword)

#%%
for word11 in eleven:
    alphaword = re.sub(r'[^A-Za-z]+','',word11)
    sixsort = sort_string(alphaword[:6]); word3 = alphaword[4:7]
    if sixsort in sorted_six and word3 in three:
        print six[sixsort], word3, word11
#        for s in get_synonyms(word3):
#            if sort_string(s) == sixsort:
#                print six[sixsort], word3, word11