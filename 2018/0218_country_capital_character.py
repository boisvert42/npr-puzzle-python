#!/usr/bin/python
'''
NPR 2018-02-18
https://www.npr.org/2018/02/18/585772621/sunday-puzzle-end-rhymes

Take the start of the name of a country and the end of that country's capital. 
Put the parts together, one after the other, and you'll get the last name of a 
character in a very popular movie. It's a character everyone knows. Who is it?
'''
import nprcommontools as nct
from nltk.corpus import wordnet as wn, gazetteers
from nltk import word_tokenize
        
#%%
common_words = nct.get_common_words()
movie_names = set()
# Via https://raw.githubusercontent.com/RaRe-Technologies/movie-plots-by-genre/master/data/tagged_plots_movielens.csv
with open(r'tagged_plots_movielens.csv','rb') as fid:
    for line in fid.readlines():
        words = word_tokenize(line)
        for w in words:
            if w[0] == w[0].upper() and w.isalpha() and len(w) > 4 and w.lower() not in common_words:
                movie_names.add(w.lower())
        
#%%
COUNTRIES = set([country for filename in ('isocountries.txt','countries.txt')
  for country in gazetteers.words(filename)])

capital_dict = dict()
for s in wn.all_synsets():
    d = s.definition()
    if 'capital' in d and 'city' in d:
        for country in COUNTRIES:
            if country in d:
                for capital in s.lemma_names():
                    if capital[0] == capital[0].upper():
                        capital_dict[country] = capital_dict.get(country,[]) + [capital]
                        
#%%
for country,capitals in capital_dict.iteritems():
    for capital in capitals:
        for i in range(1,len(country)):
            for j in range(1,len(capital)):
                c1 = country[:i]
                c2 = capital[-j:]
                name = (c1+c2).lower()
                if name in movie_names and name != country.lower() and name != capital.lower():
                    print country,capital,(c1+c2).lower()
