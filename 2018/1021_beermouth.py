#!/usr/bin/python
'''
NPR 2018-10-21
https://www.npr.org/2018/10/21/659245659/sunday-puzzle-find-the-missing-link
Take the 9 letters of BEER MOUTH. Arrange them in a 3x3 array so that 
the three lines Across, three lines Down, and both diagonals spell 
common 3-letter words. Can you do it?
'''
import sys
sys.path.append('..')
import nprcommontools as nct
import itertools

#%%
common_words = set(x.upper() for x in nct.get_common_words(source='definitions'))

WORD = 'BEERMOUTH'
for arr in itertools.permutations(WORD,len(WORD)):
    s = ''.join(arr)
    s1,s2,s3 = s[:3],s[3:6],s[6:9]
    if s1 in common_words and s2 in common_words and s3 in common_words:
        t = []
        for i in range(3):
            t1 = s1[i] + s2[i] + s3[i]
            t.append(t1)
        if t[0] in common_words and t[1] in common_words and t[2] in common_words:
            print('{0}\n{1}\n{2}'.format(s1,s2,s3))
            print()
