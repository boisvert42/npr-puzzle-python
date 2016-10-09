'''
NPR Puzzle 2016-10-02

http://www.npr.org/2016/10/02/496211559/for-a-sunny-punny-sunday-trip-how-about-a-trip-to-the-grocery-isle

Name an 11-letter occupation starting with H. 
If you have the right one, you can rearrange the 
letters to name two things a worker with this 
occupation uses — one in six letters and one in five. 
What occupation is it?
'''

import sys
sys.path.append('..')
from nprcommontools import alpha_only, sort_string, get_category_members

#%%
# 11-letter occupations starting with H
occupations = set(_x for _x in get_category_members('person') if len(alpha_only(_x)) == 11 and _x.startswith('h'))

# words of five or six letters
words = [_x for _x in get_category_members('object') if len(_x) in (5,6) and _x.isalpha()]
five_words = set(_x for _x in words if len(_x) == 5)
six_words = set(_x for _x in words if len(_x) == 6)

sorted_occupations = dict((sort_string(_x),_x) for _x in occupations)
sorted_set = frozenset(sorted_occupations.keys())

#%%
for five in five_words:
    for six in six_words:
        s_string = sort_string(five+six)
        if s_string in sorted_set:
            print sorted_occupations[s_string], five, six

