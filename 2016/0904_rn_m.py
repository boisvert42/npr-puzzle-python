'''
NPR Puzzle 2016-09-04

http://www.npr.org/2016/09/04/492557498/the-answer-remains-the-same-whichever-way-you-want-to-look-at-it

If you squish the small letters "r" and "n" too closely together, they look like an "m." 
Think of a common five-letter word with the consecutive letters "r" and "n" that becomes 
its own opposite if you change them to an "m."
'''

from nltk.corpus import brown

#%%
words = frozenset([_x.lower() for _x in brown.words() if _x.isalpha()])
rn_words = frozenset(_x for _x in words if 'rn' in _x and len(_x) == 5)

#%%
for rn_word in rn_words:
    m_word = rn_word.replace('rn','m')
    if m_word in words:
        print rn_word, m_word