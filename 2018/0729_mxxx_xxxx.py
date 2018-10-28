#!/usr/bin/python
'''
NPR 2018-07-29

https://www.npr.org/2018/07/29/633463312/sunday-puzzle-vowel-play

Think of a familiar two-word phrase in 8 letters — with 4 letters in each word. 
The first word starts with M. Move the first letter of the second word to the 
end and you'll get a regular 8-letter word, which, amazingly, other than the M, 
doesn't share any sounds with the original two-word phrase. What phrase is it?
'''
import sys
sys.path.append('..')
import nprcommontools as nct
import itertools
import requests
        
from nltk.corpus import wordnet as wn
from nltk.corpus import cmudict

#%%
words = set(x for x in wn.all_lemma_names() if x.count('_') == 0 and x.startswith('m'))
m_phrases = set()
url = 'http://www.codon.org.uk/~mjg59/tmp/wordlists/english_phrases.txt'
r = requests.get(url)
for line in r.content.split('\n'):
    line = line.strip()
    if line.count(' ') == 1 and line.split(' ')[0].startswith('m') and len(line.split(' ')[0]) == 4 and len(line.split(' ')[1]) == 4:
        m_phrases.add(line)

#%%
for m in m_phrases:
    m1,m2 = m.split(' ')
    new_word = m1 + m2[1:] + m2[0]
    if new_word in words:
        print m,new_word