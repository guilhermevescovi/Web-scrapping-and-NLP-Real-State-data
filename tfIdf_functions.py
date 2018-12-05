import nltk
import string
from collections import defaultdict
import math
import pandas

def cleaner(d):
    # the escaoe character
    escape = r'\n'
    # set stopwords
    try:
        # we try to define it
        stop_words = set(nltk.corpus.stopwords.words('italian'))
    except LookupError:
        # and if it's not present on the computer we download it
        nltk.download('stopwords')
        # and define it
        stop_words = set(nltk.corpus.stopwords.words('italian'))
    # set punctuation
    set_punt = list(string.punctuation)
    
    stemmer = nltk.stem.snowball.SnowballStemmer('italian')
    cleaned = []
    for description in d:
        cleaned_description = []
        for element in description.split(' '):
            # we delete the escape elements
            if escape == element[-2:]:
                element = element.replace(escape, '')
            for c in element:
                # delete char if it is a punctuation
                if c in set_punt:
                    element = element.replace(c,"")
            # save the string only if it isn't a stop words
            if element not in stop_words: 
                # we save the word in lowercase - so it is easier work in this way
                element = element.lower()
                # stemming
                element = stemmer.stem(element)
                cleaned_description.append(element)
        cleaned.append(cleaned_description)
    return cleaned

# we compute the tfIdf
def tfIdf_calculator(d):
    dic_count = defaultdict(lambda :defaultdict(int))
    nd = len(d)
    
    # we compute how many occurance of a word there are in a document
    for i in range(nd):
        for e in d[i]:
            dic_count[e][i]+=1
            
    # we compute the tfIdf itself and store it in a diconary
    for w in dic_count.keys():
        df = len(list(dic_count[w].keys()))
        idf = math.log10(nd/df)
        for e in dic_count[w]:
            dic_count[w][e]*=idf
    
    # we return everything as a dataframe
    return pandas.DataFrame(dic_count)