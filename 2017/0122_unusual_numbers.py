#!/usr/bin/env python
"""
NPR 2017-01-22
www.npr.org/2017/01/22/511046359/youve-got-to-comb-together-to-solve-this-one
The numbers 5,000, 8,000, and 9,000 share a property that only five integers altogether have. 
Identify the property and the two other integers that have it.
"""

# The property is that they are supervocalic (one each of aeiou).
# This code will simply try to find the other such numbers.

def is_supervocalic(w):
    '''
    Determine if a word has one each of a, e, i, o, u
    We also want it not to have a 'y'
    '''
    vowels = 'aeiou'
    for vowel in vowels:
        if w.lower().count(vowel) != 1:
            return False
    if 'y' in w.lower():
        return False
    return True

# Thanks to http://stackoverflow.com/a/19193721
def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g])
    if join: return ' '.join(words)
    return words
    
# Note that every integer greater than 100,000 has a repeated vowel
for i in range(100000):
    word = numToWords(i)
    if is_supervocalic(word):
        print i, word
