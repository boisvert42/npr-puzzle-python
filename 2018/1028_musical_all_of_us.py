'''
NPR Puzzle 2016-04-17

http://www.npr.org/2016/04/17/474509250/what-do-you-get-when-a-city-slicker-drops-his-vowels

Here's a tricky challenge from Sandy Weisz of Chicago. 
Take the name of a famous musical. Write it in upper- 
and lowercase letters, as you usually would. 
Now turn one of the characters upside-down 
and move it to another place in the title. 
The result will be the last name of a well-known 
stage performer. What is the musical, 
and who is the performer?
'''
import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members

from collections import defaultdict
import re

#%%
def flip_letter(c):
    '''
    Flip a character upside-down; return None if impossible
    '''
    flip_dict = {'a':'e','b':'q','d':'p',\
    'e':'a','h':'y','m':'w','n':'u','p':'d',\
    'q':'b','r':'J','u':'n','w':'m','y':'h',\
    'J':'r','M':'W','P':'d','W':'M','!':'i'}
    try:
        return flip_dict[c]
    except KeyError:
        return None
    
# Get a list of musicals from Wikipedia
musicals = wikipedia_category_members('Broadway_musicals')
#musicals = musicals.union(wikipedia_category_members('Off-Broadway_musicals'))
#musicals = musicals.union(wikipedia_category_members('American musical films'))

# Get a list of famous names
names = defaultdict(list)
with open(r'../wordlists/FamousNames.txt','rb') as fid:
    for line in fid.readlines():
        line = line.strip()
        name,score = line.split('\t')
        score = int(score)
        if score >= 90:# and ' ' in name:
            names[name.lower().split(' ')[-1]].append(name)
name_set = frozenset(names.keys())
#%%
# Go through musicals and look for names that fit
for musical in musicals:
    musical_nospace = re.sub(r'[^A-Za-z!]+','',musical)
    for i in range(len(musical_nospace)):
        letter = musical_nospace[i]
        if flip_letter(letter) is not None:
            l2 = flip_letter(letter).lower()
            musical_letter_missing = musical_nospace[:i]+musical_nospace[i+1:]
            musical_letter_missing = musical_letter_missing.lower()
            for j in range(len(musical_nospace)):
                name = musical_letter_missing[:j] + l2 + musical_letter_missing[j:]
                #print name                
                if name in name_set:
                    print '{0} -> {1} ({2})'.format(musical,name,', '.join(names[name]))