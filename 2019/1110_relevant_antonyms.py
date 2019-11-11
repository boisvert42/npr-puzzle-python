#!/usr/bin/env python
"""
NPR 2019-11-10
https://www.npr.org/2019/11/10/777941999/sunday-puzzle-7-letters

Think of two five-letter words that are opposites. One of them begins with E, the other ends with E. 
Drop both E's. The remaining eight letters can be rearranged to spell a new word that is relevant. 
What are these three words?
"""
import sys
sys.path.append('..')
import nprcommontools as nct
common_words = nct.get_common_words()
#%%
five_letter_words = frozenset([x for x in common_words if len(x) == 5 and (x.startswith('e') or x.endswith('e'))])
eight_letter_words = frozenset([x for x in common_words if len(x) == 8])
eight_dict = nct.make_sorted_dict(eight_letter_words)
for w1 in five_letter_words:
    antonyms = nct.get_antonyms(w1).intersection(five_letter_words)
    for a1 in antonyms:
        sorted_string = nct.sort_string((w1+a1).replace('e', '', 2))
        try:
            print(w1, a1, eight_dict[sorted_string])
        except:
            pass
