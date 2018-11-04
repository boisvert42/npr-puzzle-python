'''
NPR Puzzle 2018-11-04

https://www.npr.org/2018/11/04/663572384/sunday-puzzle-can-you-convert-these-euros

Think of an article of apparel in eight letters. Drop the last 2 letters. 
Move what are the now the last 2 letters to the front. 
You'll get an article of apparel in 6 letters. What is it?
'''

# Note: this code does not find the correct answer, as the eight-letter word in question is not in Wordnet.
import sys
sys.path.append('..')
import nprcommontools as nct


#%%
# Get articles of clothing
apparel = nct.get_category_members('article_of_clothing')

for a1 in apparel:
    if len(a1) == 8:
        a2 = a1[4:6] + a1[:4]
        if a2 in apparel:
            print(a1,a2)
