'''
NPR Puzzle 2016-07-03

http://www.npr.org/2016/07/03/484502061/just-in-time-for-the-4th-heres-a-puzzle-tailor-made-for-the-patio

[Take] the word SHALL. Divide it into two parts, so that the start of it starts one word 
and the end of it ends another word — and those two words are opposites. The dividing point 
is for you to discover. There are three different solutions. I want you to find all three.

'''

import sys
sys.path.append('..')
from nprcommontools import get_antonyms
from nltk.corpus import wordnet as wn
#%%
BASE_WORD = 'shall'
mylen = len(BASE_WORD)

s_words = [x for x in wn.all_lemma_names() if x.startswith(BASE_WORD[0])]
for word in s_words:
    ants = get_antonyms(word)
    for a in ants:
        for i in range(1,mylen):
            w1,w2 = BASE_WORD[:i],BASE_WORD[i:]
            if word.startswith(w1) and a.endswith(w2):
                print word,a