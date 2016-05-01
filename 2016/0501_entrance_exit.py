'''
NPR Puzzle 2016-05-01

http://www.npr.org/2016/05/01/476310217/follow-the-rhyme-to-solve-the-mystery-of-the-missing-pair

Think of a word that means "entrance." 
Interchange the second and fourth letters, 
and you'll get a new word that means "exit." 
What words are these?
'''
# Wordnet doesn't list these two words as synonyms
# There aren't too many possibilities anyway
from nltk.corpus import brown
words = frozenset([x.lower() for x in brown.words() if x.isalpha() and len(x) >= 4])

#%%
for word in words:
    word2 = word[0] + word[3:0:-1] + word[4:]
    if word2 in words and word != word2:
        print word, word2