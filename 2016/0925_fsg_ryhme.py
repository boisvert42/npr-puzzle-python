'''
NPR Puzzle 2016-09-25

http://www.npr.org/2016/09/25/495308799/want-to-get-an-a-better-know-your-words-backward-and-forward

Take the words DOES, TOES and SHOES. 
They all end in the same three letters, but none of them rhyme. 
What words starting with F, S and G have the same property? 
The F and S words are four letters long, and the G word is five letters. 
They all end in the same three letters.
'''

import sys
sys.path.append('..')
import rhyme

#%%
f_words = [_x for _x in rhyme._cdict_words if len(_x) == 4 and _x.startswith('f')]
for f_word in f_words:
    last_three = f_word[-3:]
    s_word = 's' + last_three
    if s_word in rhyme._cdict_words:
        if not rhyme.does_rhyme(f_word,s_word):
            g_words = [_x for _x in rhyme._cdict_words if _x.startswith('g') and _x.endswith(last_three) and len(_x) == 5]
            for g_word in g_words:
                if not rhyme.does_rhyme(f_word,g_word) and not rhyme.does_rhyme(s_word,g_word):
                    print f_word,s_word,g_word
