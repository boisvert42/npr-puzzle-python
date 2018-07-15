#!/usr/bin/python
'''
NPR 2018-07-15

https://www.npr.org/series/4473090/sunday-puzzle

Name a famous person from Chicago — first and last names. The last name ends in an E. 
Change the E to an I and rearrange the letters in just the last name to get a famous actor — 
whose first name is the same as the first person's. Who are these people?
'''
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
# Get famous names
names = [x for x in nct.get_famous_names() if x.count(' ') == 1]

#%%
name_dict = dict()
for name in names:
    fn,ln = name.split(' ')
    ln2 = nct.sort_string(ln.lower())
    name2 = fn.lower() + ' ' + ln2
    value = name_dict.get(name2,[])
    value.append(name)
    name_dict[name2] = value
    
#%%
for n1 in name_dict.iterkeys():
    fn,ln = n1.split(' ')
    if 'e' in ln:
        ln2 = ln.replace('e','i',1)
        n2 = fn + ' ' + ln2
        try:
            name_dict[n2]
            print name_dict[n1], name_dict[n2]
        except KeyError:
            pass