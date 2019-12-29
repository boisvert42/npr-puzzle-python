import sys
sys.path.append('..')
import nprcommontools as nct
from nltk.corpus import wordnet as wn
#%%
names = nct.get_famous_names()
names = [x for x in names.keys() if x.count(' ') == 1 and len(x.split(' ')[0]) == 5 and len(x.split(' ')[1]) == 6 and 'i' in x.lower()]
#%%
words_phrases_11 = [nct.alpha_only(x.lower()) for x in wn.all_lemma_names() if len(nct.alpha_only(x)) == 11 and 'w' in x.lower()]
wp_dict = nct.make_sorted_dict(words_phrases_11)
wp_set = frozenset(wp_dict.keys())
#%%
for name in names:
    name_w = name.lower().replace('i', 'w', 1)
    sorted_name_w = nct.sort_string(nct.alpha_only(name_w))
    if sorted_name_w in wp_set:
        print(name, wp_dict[sorted_name_w])
