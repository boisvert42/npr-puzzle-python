#!/usr/bin/env python
"""
NPR 2016-01-03

http://www.npr.org/2016/01/03/461707406/o-say-can-you-see-what-the-2-blanks-might-be

This is a variation on the old word ladder puzzle. 
The object is to change WHOLE to HEART by either adding or subtracting one letter at a time, 
making a new, common, uncapitalized word at each step.

For example, you can change RED to ROSE in five steps. 
Starting with RED, you could add a U, making RUED; drop the D, leaving RUE; 
add an S, making RUSE; add an O, making ROUSE, and then drop the U, leaving ROSE.

Changing or rearranging letters is not allowed, 
neither are plurals or verbs formed by adding -S. 
No word in the chain can have fewer than three letters.
"""
from nltk.corpus import words
ALL_WORDS = frozenset(words.words())

# Add/delete code courtesy of http://norvig.com/spell-correct.html
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + inserts)
   
def known_edits(word):
    return set([x for x in edits1(word) if len(x) >= 3 and x in ALL_WORDS])

first_word = 'whole'
last_word = 'heart'

#%%
word_to_path = {first_word:[first_word]}
found_words = set([first_word])
keep_going_flag = True

while keep_going_flag:
    for word in found_words:
        new_set = set()
        #print word
        if word == last_word:
            print word_to_path[word]
            keep_going_flag = False
            break
        new_words = known_edits(word)
        for new_word in new_words.difference(found_words):
            word_to_path[new_word] = word_to_path[word] + [new_word]
            new_set.add(new_word)
        found_words = found_words.union(new_set)