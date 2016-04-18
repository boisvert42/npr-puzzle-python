#!/usr/bin/env python
'''
NPR 2016-03-13

http://www.npr.org/2016/03/13/470220527/feeling-puzzled-just-take-an-amble-down-d-st

Take the name of a well-known actress.
Her first name starts with the three-letter abbreviation for a month.
Replace this with the three-letter abbreviation of a different month,
and you'll get the name of a famous poet. Who are these two people?
'''
import datetime
from collections import defaultdict

month_abbrs = set()
for i in range(1,13):
    dt = datetime.datetime.strptime(str(i),'%m')
    month_abbrs.add(dt.strftime('%b').lower())
   
#%%
# Read in famous names
month_names = defaultdict(list)
with open(r'../wordlists/FamousNames.txt','rb') as fid:
    for line in fid.readlines():
        line = line.strip().lower()
        name,score = line.split('\t')
        for month in month_abbrs:
            if name.startswith(month) and score >= 90:
                name2 = name[3:]
                month_names[name2].append(name)
#%%
for name in month_names.iterkeys():
    if len(month_names[name]) >= 2:
        print month_names[name]