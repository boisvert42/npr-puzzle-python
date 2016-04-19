#!/usr/bin/env python
"""
NPR 2016-01-10

http://www.npr.org/2016/01/10/462517951/looking-for-something-to-wear-just-scramble-some-letters

Name a unit of measurement. Remove two consecutive letters. 
The letters that remain can be rearranged to name what this measurement measures. What is it?
"""
import sys
sys.path.append('..')
from nprcommontools import get_category_members

from nltk.corpus import wordnet as wn

units_of_measurement = get_category_members('measure')
        
for measure in units_of_measurement:
    synsets = wn.synsets(measure)
    for synset in synsets:
        for word in synset.definition().split(' '):
            if len(word) == len(measure) - 2 and set(word).issubset(set(measure)) and len(word)>2:
                print word,measure