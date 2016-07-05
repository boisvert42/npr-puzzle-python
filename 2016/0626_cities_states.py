'''
NPR Puzzle 2016-06-26

http://www.npr.org/2016/06/26/483521883/welcome-to-an-affair-of-phrases-each-entwined-by-a-tiny-of

Think of two well-known American cities, each five letters long. 
The first two letters of the first city are the state postal abbreviation of the second city. 
And the first two letters of the second city are the state postal abbreviation of the first city. 
What two cities are these?
'''

from nltk.corpus import gazetteers

# Get list of abbreviations from Gazetteers
state_abbrs = frozenset(abbr for abbr in gazetteers.words('usstateabbrev.txt') if len(abbr) ==2)

# Get list of cities from Gazetteers
cities = frozenset(city for city in gazetteers.words('uscities.txt') if len(city) == 5)

for city in cities:
    if city.upper()[:2] in state_abbrs:
        print city
