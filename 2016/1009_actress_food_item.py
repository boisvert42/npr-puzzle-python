'''
NPR Puzzle 2016-10-09

http://www.npr.org/2016/10/09/497173317/these-letters-dont-li

Name a famous actress of the past — first and last names, 10 letters altogether. 
Change one letter in the first name and one letter in the last. The result is a 
two-word phrase naming a food item often found in a kitchen cabinet or refrigerator. 
What is it?
'''

import sys
sys.path.append('..')
from nprcommontools import alpha_only, get_famous_names, get_category_members
from nltk.corpus import names, brown

#%%
# Ten-letter famous names
female_names = names.words('female.txt')
famous_names = frozenset(_x for _x in get_famous_names(95) 
                if len(alpha_only(_x))==10 
                and _x.count(' ') == 1
                and _x.split(' ')[0] in female_names)
                
# Foods
foods = get_category_members('food')

# "Common" words from the Brown corpus
brown_words = frozenset(_x for _x in brown.words() if _x.isalpha())

# Thank you http://norvig.com/spell-correct.html
def edits1(word):
    # Return anything that's a letter change from "word"
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    return set(replaces).intersection(brown_words)
    
#%%
for name in famous_names:
    first,last = name.lower().split(' ')
    first_replaces = edits1(first); last_replaces = edits1(last)
    for f in first_replaces:
        for l in last_replaces:
            if '{0}_{1}'.format(f,l) in foods:
                print name, '{0}_{1}'.format(f,l)

