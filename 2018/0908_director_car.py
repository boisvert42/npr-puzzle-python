#!/usr/bin/python
'''
NPR 2018-07-22

https://www.npr.org/2018/07/22/630812232/sunday-puzzle-part-human

Name two parts of the human body. Say them one out loud after the other. 
The result, phonetically, will name something delicious to eat, in 7 letters. What is it? 
'''
import sys
sys.path.append('..')
import nprcommontools as nct

#%%
# Get famous names
names = nct.get_famous_names()
name_dict = dict()
for name in names:
    name_dict[nct.alpha_only(name.lower())] = name

#%%
# Get cars
cars = set()
years = (1970,1980,1990,2000,2010)
for year in years:
    category = '{0}s_automobiles'.format(year)
    year_cars = nct.wikipedia_category_members(category,1)
    for yc in year_cars:
        model = yc.split(' ')[-1]
        if len(model) == 6:
            cars.add(model.lower())

#%%
for n1,name in name_dict.iteritems():
    for car in cars:
        if car in n1 and car not in name.lower():
            print name,car