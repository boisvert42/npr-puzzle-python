import unicodedata
import time
import requests

def remove_accents(s):
    '''
    Remove diacritics from a string
    '''
    return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))

def wikipedia_category_members(category):
    '''
    Get category members from Wikipedia
    '''
    category_members = set()
    # Convert spaces to underscore
    category = category.replace(' ','_')
    cmcontinue_str = ''
    cmcontinue = True
    while cmcontinue:
        url = "http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{0}&cmlimit=500&format=json&cmnamespace=0&cmtype=page&cmcontinue={1}".format(category,cmcontinue_str)
        r = requests.get(url)
        json = r.json()
        cat_member_list = json['query']['categorymembers']
        for row in cat_member_list:
            title = remove_accents(row['title'])
            # Remove trailing parens, if any
            if title[-1] == ')' and title.find(' (') > -1:
                ix = title.find(' (')
                title = title[:ix]
            category_members.add(title)
        try:
            cmcontinue_str = json['continue']['cmcontinue']
            time.sleep(1)
        except KeyError:
            cmcontinue = False
    return category_members
#END wikipedia_category_members()

def letter_shift(l,n):
    '''
    letter_shift(l,n): shift letter l by n places
    
    NOTE: always returns a lowercase letter
    '''
    l = l.lower()
    assert type(n) == int
    assert len(l) == 1
    
    new_ord = ord(l) + n
    while new_ord > 122:
        new_ord = new_ord - 26
    return chr(new_ord)

def get_category_members(name):
    '''
    Use NLTK to get members of a category
    '''
    from nltk.corpus import wordnet as wn
    members = set()
    synsets = wn.synsets(name)
    for synset in synsets:
        members = members.union(set([w for s in synset.closure(lambda s:s.hyponyms(),depth=10) for w in s.lemma_names()]))
    return members

