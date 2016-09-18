'''
NPR Puzzle 2016-09-18

http://www.npr.org/2016/09/18/494382869/do-remember-the-first-3-letters-of-september

Think of a familiar three-word phrase in the form "___ and ___." 
Drop the "and." Then move the last word to the front to form a single word 
that means the opposite of the original phrase.
Here's a hint: The ending word has seven letters. What is it?
'''

from nltk.corpus import wordnet as wn

and_phrases = frozenset([x for x in wn.all_lemma_names() if '_and_' in x and len(x) == 12])
seven_letter_words = frozenset([x for x in wn.all_lemma_names() if x.isalpha() and len(x) == 7])

for phrase in and_phrases:
    words = phrase.split('_')
    word = words[2]+words[0]
    if word in seven_letter_words:
        print phrase, word
