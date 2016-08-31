'''
NPR Puzzle 2016-08-28

www.npr.org/2016/08/28/491699329/3-3-8-it-does-in-this-weeks-puzzle

What one-syllable word in 7 letters becomes a 
four-syllable word by inserting the consecutive 
letters IT somewhere inside?
'''
import sys
sys.path.append('..')
import rhyme

#%%
# Get a list of common seven- and nine-letter words
seven_letter_words = frozenset([_x.lower() for _x in rhyme._cdict if _x.isalpha() and len(_x) == 7])
nine_letter_words = frozenset([_x.lower() for _x in rhyme._cdict if _x.isalpha() and len(_x) == 9 and 'it' in _x])

#%%
for nine in nine_letter_words:
    if rhyme.syllables(nine) == 4:
        ix = nine.find('it')
        seven = nine[:ix] + nine[ix+2:]
        if rhyme.syllables(seven) == 1:
            if seven in seven_letter_words:    
                print seven, nine
