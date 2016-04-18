#!/usr/bin/env python
'''
NPR 2016-04-03

http://www.npr.org/2016/04/03/472825113/got-2-words-in-the-same-category-its-rhymin-time

Take the word EASY: Its first three letters — E, A and S — 
are the fifth, first, and nineteenth letters, respectively, 
in the alphabet. If you add 5 + 1 + 19, you get 25, 
which is the value of the alphabetical position of Y, 
the last letter of EASY.

Can you think of a common five-letter word that works in 
the opposite way — in which the value of the alphabetical 
positions of its last four letters add up to the value of 
the alphabetical position of its first letter?
'''
from nltk.corpus import brown


def letter_value(s):
    '''
    Return the sum of letter values of a string
    '''
    mysum = 0
    for char in s.upper():
        if char >= 'A' and char <= 'Z':
            mysum = mysum + ord(char) - 64
    return mysum
    
#%%
# Words from the Brown corpus
words = set([x.lower() for x in brown.words() if len(x) == 5 and x.isalpha()])
    
#%%
for word in words:
    if letter_value(word[0]) == letter_value(word[1:]):
        print word
