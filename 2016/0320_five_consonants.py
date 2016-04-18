"""
NPR 2016-03-20

http://www.npr.org/2016/03/20/471102829/first-and-last-two-letters-are-key-to-solve-this-puzzle-thats-not-so-easy

Think of a common nine-letter word that contains five 
consecutive consonants. Take three consecutive consonants 
out of these five and replace them with vowels to form 
another common nine-letter word. What is it?

"""
from nltk.corpus import brown
import re

words = set([x.lower() for x in brown.words() if len(x) == 9 and x.isalpha()])

#%%
for word in words:
    match = re.search(r'[^aeiouy]{5}',word)
    if match is not None:
        #print word, match
        index1, index2 = match.start(), match.end()
        re2 = word[:index1] + r'.*[aeiou]{3}.*' + word[index2:]
        for word2 in words:
            if re.search(re2,word2) is not None:
                print word, word2