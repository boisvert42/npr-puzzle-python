"""
NPR 2019-01-20
https://www.npr.org/2019/01/20/686968039/sunday-puzzle-youre-halfway-there

This challenge comes from listener Steve Baggish of Arlington, Mass. 
Take the name of a classic song that became the signature song of the artist who performed it. 
It has two words; five letters in the first, three letters in the second. 
The letters can be rearranged to spell two new words. One is a feeling. 
The other is an expression of that feeling. What song is it?
"""

import requests

url = 'https://cdn.jsdelivr.net/gh/fivethirtyeight/data@master/classic-rock/classic-rock-raw-data.csv'
r = requests.get(url)
csv_data = r.content.decode('utf-8')

#%%
songs = set()
lines = csv_data.split('\r')
for line in lines:
    song = line.split(',')[1]
    if song.count(' ') == 1:
        if len(song.split(' ')[0]) == 5 and len(song.split(' ')[1]) == 3:
            songs.add(song)
print(songs)
