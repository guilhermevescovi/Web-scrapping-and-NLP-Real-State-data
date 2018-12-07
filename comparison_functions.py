import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# we extract the trop three element from a dataframe along with their position
def top3extractor(df):

    # we get the three values
    result_array = sorted(df.values.flatten(), reverse = True)
    top_3 = result_array[:3]
    
    # and we retrive their position
    listj = []
    for i in range(len(df.values)):
        for k in range(len(df.values[i])):
            if df.values[i][k] in top_3:
                listj.append(list([i,k, df.values[i][k]]))
                
    return pd.DataFrame(listj,columns = ['feature index','description index','Jaccard index'])



# we prepare the list of words to build the wordcloud
def word_clouder(l1,i,l2,j,list_description):
    
    s1 = l1[i]
    s2 = l2[j]
    # we prepare the stopwords to remove
    try:
        # we try to define it
        stop_words = set(nltk.corpus.stopwords.words('italian'))
    except LookupError:
        # and if it's not present on the computer we download it
        nltk.download('stopwords')
        # and define it
        stop_words = set(nltk.corpus.stopwords.words('italian'))
    
    list_words = []
    
    # we remove special character and stopwords, and append the word in a list
    for k in (s1 & s2):
        tlist = list_description[k].split(" ")
        while '' in tlist:
            tlist.remove('')
        while '\n' in tlist:
            tlist.remove('\n')
        while '\n\n' in tlist:
            tlist.remove('\n\n')
        for word in tlist:
            if word not in stop_words:
                list_words.append(word)
    
    clouder(list_words,str(i)+' '+str(j))

# given a set of words and the index of the clusters they come from (wirte the title) we create the wordcloud
def clouder(list_words,clusters_index):
        
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(' '.join(list_words))
    plt.figure(figsize=(20,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title('Word cloud for cluster intersection '+clusters_index)
    plt.show()    