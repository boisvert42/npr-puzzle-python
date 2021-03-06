#!/usr/bin/env python
"""
NPR 2017-02-05
http://www.npr.org/2017/02/05/513476303/sunday-puzzle-once-upon-a-time-these-names-would-have-been-easy-to-recall

Name a prominent figure in a fairy tale. Write this in all capital letters. 
Add a stroke to one letter and rearrange the result. 
You'll name another prominent figure in a fairy tale. 
What two fairy tale figures are these?
"""

import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members, sort_string, alpha_only

#%%
# Letters that we think can turn into another one by adding a stroke
stroked_letters = {
    'F':'E',
    'O':'Q',
    'P':'RB',
    'I':'TPDL',
    'T':'I',
    'R':'B',
    'U':'O',
    'C':'GO'
}

#%%
fairy_tale_characters = wikipedia_category_members('Characters_in_fairy_tales',max_depth=3)
fairy_tale_characters = fairy_tale_characters.union(wikipedia_category_members('Fairy_tales',max_depth=3))

#%%
# Lots of things in here are separated by "and"s.  Let's split those
f2 = copy.deepcopy(fairy_tale_characters)
for f in f2:
    if ' and ' in f:
        arr = f.split(' and ')
        for w in arr:
            w2 = w
            w = w.replace('the ','')
            w = w.replace('The ','')
            w = w.strip()
            w2 = w2.strip()
            #print w
            fairy_tale_characters.add(w)
            fairy_tale_characters.add(w2)

ft_dict = dict((sort_string(alpha_only(x.upper())),x) for x in fairy_tale_characters)

#%%
for character in fairy_tale_characters:
    char_upper = alpha_only(character.upper())
    for i in range(len(char_upper)):
        letter = char_upper[i]
        if letter in stroked_letters:
            for letter2 in stroked_letters[letter]:
                stroked_sorted = sort_string(char_upper[:i]+letter2+char_upper[i+1:])
                if stroked_sorted in ft_dict:
                    print character, ft_dict[stroked_sorted]

