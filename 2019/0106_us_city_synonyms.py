#%%
"""
NPR 2019-01-06
https://www.npr.org/2019/01/06/682575357/sunday-puzzle-stuck-in-the-middle

Name a major U.S. city in 10 letters. If you have the right one, you can rearrange its letters to get two 5-letter words that are synonyms. What are they?
"""

import sys
sys.path.append('..')
import nprcommontools as nct
from nltk.corpus import gazetteers

#%%
COMMON_WORDS = frozenset(x for x in nct.get_common_words() if len(x) == 5)

#%%
US_CITIES = set(nct.alpha_only(x.lower()) for x in gazetteers.words('uscities.txt') if len(nct.alpha_only(x)) == 10)
city_dict = nct.make_sorted_dict(US_CITIES)

#%%
for c1 in COMMON_WORDS:
    my_synonyms = nct.get_synonyms(c1)
    for c2 in my_synonyms:
        sort_word = nct.sort_string(''.join(c1+c2))
        if sort_word in city_dict:
            print(c1,c2,city_dict[sort_word])
