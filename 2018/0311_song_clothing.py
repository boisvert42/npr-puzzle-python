#!/usr/bin/env python
"""
NPR 2018-03-11
https://www.npr.org/2018/03/11/592267545/sunday-puzzle-just-drop-it
Name a common article of apparel in 3 letters and another in 4 letters. 
Rearrange all 7 letters to name a well-known three-word song title. What is it?
"""

import sys
sys.path.append('..')
import nprcommontools as nct
import requests
import csv

#%%
# Get list of rock songs
rock_songs_url = 'https://cdn.rawgit.com/fivethirtyeight/data/14b0e3df/classic-rock/classic-rock-song-list.csv'
r = requests.get(rock_songs_url)
s = r.content
s = s.replace('\r','\n')
fid = csv.reader(csv.StringIO(s))
songs = set()
row = fid.next()
while row:
    songs.add(row[0])
    try:
        row = fid.next()
    except StopIteration:
        row = None
song_dict = nct.make_sorted_dict(songs)        
#%%
apparel = nct.get_category_members('article_of_clothing')
for a1 in apparel:
    for a2 in apparel:
        if a1<a2:
            a1_a2_lower = nct.sort_string(nct.alpha_only(a1+a2)).lower()
            try:
                print song_dict[a1_a2_lower],a1,a2
            except KeyError:
                pass
