#!/usr/bin/python
'''
NPR 2017-07-02
http://www.npr.org/2017/07/02/535224912/sunday-puzzle-follow-my-lead

Think of a common girl's name. Write it in all capital letters. 
Rotate one of these letters 90 degrees and another of the letters 180 degrees. 
The result will name a make of a car. What is it?
'''
import sys
sys.path.append('..')
from nprcommontools import wikipedia_category_members
from nltk.corpus import names

#%%
girls_names = [_.upper() for _ in names.words("female.txt")]
car_makes = [_.upper() for _ in wikipedia_category_members('Car_brands',max_depth=1)]

#%%
rot_90 = {'C':'U','H':'I','N':'Z'}
s = rot_90.items()
for k,v in s:
    rot_90[v] = k
          
rot_180 = {'M':'W','W':'M'}

key_90 = set(rot_90.keys())
key_180 = set(rot_180.keys())

for car in car_makes:
    car_set = set(car)
    s1 = car_set.intersection(key_90)
    s2 = car_set.intersection(key_180)
    if s1 and s2:
        for l1 in s1:
            for l2 in s2:
                name = car.replace(l1,rot_90[l1])
                name = name.replace(l2,rot_180[l2])
                if name in girls_names:
                    print name, car