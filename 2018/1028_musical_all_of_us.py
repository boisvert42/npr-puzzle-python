'''
NPR Puzzle 2018-10-28

https://www.npr.org/2018/10/28/660936138/sunday-puzzle-row-row-row

Think of a famous Broadway musical in two words. 
Change one letter in it to the preceding letter of the alphabet — 
so B would become A, C would become B, etc. 
Remove the space so you have a solid word. 
The result will name something that all of us are part of. What is it?
'''
import sys
sys.path.append('..')
import nprcommontools as nct

from nltk.corpus import wordnet as wn
import re

#%%
# Get a list of musicals from Wikipedia
musicals = set(x for x in nct.wikipedia_category_members('Broadway_musicals') if x.count(' ') == 1)
#musicals = musicals.union(wikipedia_category_members('Off-Broadway_musicals'))
#musicals = musicals.union(wikipedia_category_members('American musical films'))

words = set(x for x in wn.all_lemma_names() if x.count('_') == 0)
#%%
# Go through musicals and look for ones that work
for musical in musicals:
    musical_nospace = re.sub(r'[^A-Za-z]+','',musical).lower()
    for i in range(len(musical_nospace)):
        letter = musical_nospace[i]
        myword = musical_nospace[:i] + nct.letter_shift(letter,-1) + musical_nospace[i+1:]
        if myword in words:
            print(musical,myword)
