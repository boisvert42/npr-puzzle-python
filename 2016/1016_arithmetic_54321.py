#!/usr/bin/env python
"""
NPR 2016-10-16

http://www.npr.org/2016/10/16/497861459/when-it-comes-to-the-puzzle-dont-mail-it-in-just-exchange-a-letter

Take the digits 5, 4, 3, 2 and 1, in that order. Using those digits and the four arithmetic signs — 
plus, minus, times and divided by — you can get 1 with the sequence 5 - 4 + 3 - 2 - 1. 
You can get 2 with the sequence (5 - 4 + 3 - 2) x 1.

The question is ... how many numbers from 1 to 40 can you get using the digits 5, 4, 3, 2, and 1 
in that order along with the four arithmetic signs? You can group digits with parentheses, as in the example. 
"""
from __future__ import division
from itertools import combinations_with_replacement, permutations

def add_parens(s):
    '''
    Given a string s which we assume to be an arithmetic expression (e.g. 5+4-2)
    we add parentheses to it in all possible ways
    and return a generator of the results
    '''
    # Indexes of all the digits
    digit_indexes = [s.index(_x) for _x in s if _x.isdigit()]
    # The first parenthesis goes before any digit except the last
    for i in range(len(digit_indexes[:-1])):
        f = digit_indexes[i]
        # The second parenthesis goes after any digit after the first
        for j in range(i+1,len(digit_indexes)):
            l = digit_indexes[j]+1
            yield s[:f] + '(' + s[f:l] + ')' + s[l:]
#%%
NUMBERS = map(str,range(5,0,-1))
SYMBOLS ='+*/-'
TARGET_NUMBERS = frozenset(range(1,41))
results = dict()
for operation_combination in combinations_with_replacement(SYMBOLS,4):
    for operation_permutation in permutations(operation_combination,4):
        string_to_evaluate = ''
        for i in range(len(SYMBOLS)):
            string_to_evaluate += NUMBERS[i] + operation_permutation[i]
        string_to_evaluate += NUMBERS[4]
        result = eval(string_to_evaluate)
        if result in TARGET_NUMBERS and result not in results.keys():
            results[int(result)] = string_to_evaluate
            
        # Now add all possible placements of parentheses as well
        # I think we can restrict ourselves to two sets of parens
        # Actually, two sets doesn't help anything
        for paren_string in add_parens(string_to_evaluate):
            try:                
                result = eval(paren_string)
            except ZeroDivisionError:
                result = 0
            if result in TARGET_NUMBERS and result not in results.keys():
                results[int(result)] = paren_string
#            for double_paren_string in add_parens(paren_string):
#                try:                
#                    result = eval(double_paren_string)
#                except ZeroDivisionError:
#                    result = 0
#                if result in TARGET_NUMBERS and result not in results.keys():
#                    results[int(result)] = double_paren_string
                    
s = ''
for k, v in results.iteritems():
    s += '{0}: {1}\n'.format(k, v)
    
print s
print
print 'Missing numbers: {0}'.format(TARGET_NUMBERS.difference(set(results.keys())))
