import unicodedata
import time
import requests

def sort_string(s):
    '''
    Sort a string
    '''
    return ''.join(sorted(s))

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
        url = "http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{0}&cmlimit=500&format=json&cmnamespace=0&cmtype=page&utf8=&cmcontinue={1}".format(category,cmcontinue_str)
        r = requests.get(url)
        json = r.json()
        cat_member_list = json['query']['categorymembers']
        for row in cat_member_list:
            try:
                title = remove_accents(row['title'])
                # Remove trailing parens, if any
                if title[-1] == ')' and title.find(' (') > -1:
                    ix = title.find(' (')
                    title = title[:ix]
                category_members.add(title)
            except UnicodeDecodeError as e:
                print e, row['title']
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
    
def get_synonyms(word):
    '''
    Use wordnet to get synonyms
    '''
    from nltk.corpus import wordnet as wn
    syns = set()
    synsets = wn.synsets(word)
    for synset in synsets:
        for w in synset.lemma_names():
            if w != word:
                syns.add(w)
    return syns

def get_category_members(name):
    '''
    Use NLTK to get members of a category
    '''
    from nltk.corpus import wordnet as wn
    import six
    members = set()
    # We behave slightly differently if `name` is a string or synset
    if isinstance(name, six.string_types):
        synsets = wn.synsets(name)
    else: # we have a synset
        synsets = [name]
    for synset in synsets:
        members = members.union(set([w for s in synset.closure(lambda s:s.hyponyms(),depth=10) for w in s.lemma_names()]))
    return members
    
def get_hypernyms(name):
    '''
    List the hypernyms of a word or subset
    '''
    from nltk.corpus import wordnet as wn
    import six
    members = set()
    # We behave slightly differently if `name` is a string or synset
    if isinstance(name, six.string_types):
        synsets = wn.synsets(name)
    else: # we have a synset
        synsets = [name]
    for synset in synsets:
        members = members.union(set([w for s in synset.closure(lambda s:s.hypernyms(),depth=10) for w in s.lemma_names()]))
    return members

def get_famous_names(minscore=90):
    '''
    Read names from FamousNames.txt with the given minimum score
    
    Returns a dict of name -> score
    '''
    return_dict = dict()
    import os
    this_dir, this_filename = os.path.split(__file__)
    famous_names_path = os.path.join(this_dir,'wordlists','FamousNames.txt')
    with open(famous_names_path,'rb') as fid:
        for line in fid.readlines():
            line = line.strip()
            name,score = line.split('\t')
            score = int(score)
            if score >= minscore:
                return_dict[name] = score
    return return_dict
