# -*- coding: utf-8 -*-
"""
NPR 2016-04-10

http://www.npr.org/2016/04/10/473649171/rearrange-the-letters-in-these-names-to-solve-this-puzzle

Name something in eight letters that's usually bought in pairs. 
Change the second letter to the letter two spaces later in the 
alphabet, and you'll get a new word that names something else 
that's usually bought in pairs. Both words are plurals. 
What are they?
"""
import sys
sys.path.append('..')
from nprcommontools import letter_shift

from nltk.corpus import brown

            
#%%
# Get a list of words from the Brown corpus
words = set([x for x in brown.words() if len(x) == 8])
            
#%%
# For eeach word, see if shifting the second letter by 2
# results in a new word
for word in words:
    word2 = word[:1] + letter_shift(word[1],2) + word[2:]
    if word2 in words:
        print word,word2
