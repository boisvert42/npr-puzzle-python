#!/usr/bin/python
'''
NPR 2018-05-20

https://www.npr.org/2018/05/20/612119230/sunday-puzzle-not-as-advertised

Take the title of a famous Hollywood flop. Change an A to an R, 
then rearrange the letters to spell a famous box office hit — 
which went on to spawn sequels. What films are these?
'''
import requests
import csv
import sys
import HTMLParser

sys.path.append('..')
import nprcommontools as nct
        
#%%
# Get list of movies from GitHub
url = 'https://cdn.rawgit.com/fivethirtyeight/data/ae8512ed/bechdel/movies.csv'
r = requests.get(url)
csv_data = r.content
csv_list = csv_data.split('\r')
data = list(csv.reader(csv_list))

#%%
parser = HTMLParser.HTMLParser()
movies_a = set()
movies_r = set()
for row in data:
    movie = parser.unescape(row[2].lower())
    if 'a' in movie:
        movies_a.add(movie)
    if 'r' in movie:
        movies_r.add(movie)
        
#%%
movies_r_dict = nct.make_sorted_dict(movies_r)
#%%
for m in movies_a:
    movie_r_sorted = nct.sort_string(nct.alpha_only(m.lower().replace('a','r',1)))
    if movie_r_sorted in movies_r_dict:
        movie_r = movies_r_dict[movie_r_sorted]
        print m,movie_r

