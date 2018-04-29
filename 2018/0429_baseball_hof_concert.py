#!/usr/bin/env python
"""
NPR 2018-04-29
https://www.npr.org/2018/04/29/606172433/sunday-puzzle-the-same-but-different

Name a famous player in the Baseball Hall of Fame. 
Take a letter out of the last name and move it into the first name. 
The result will name something you might see at a concert. What is it?
"""
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
hof = nct.wikipedia_category_members('National_Baseball_Hall_of_Fame_inductees')
#%%
common_words = nct.get_common_words()
#%%
for n in hof:
    if n.count(' ') == 1:
        first,last = n.lower().split(' ')
        for i in range(len(last)):
            letter = last[i]
            last2 = last[:i] + last[i+1:]
            if last2 in common_words:
                for j in range(len(first)):
                    first2 = first[:j] + letter + first[j:]
                    if first2 in common_words:
                        print n, first2, last2
