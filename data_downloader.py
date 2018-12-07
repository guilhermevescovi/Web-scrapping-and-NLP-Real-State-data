import requests
import bs4
import time
import re

# we define a function to download the annoucnements
def downloader():
    page_number = 1
    list_features_all_c = []
    descriptions_list = []
    # we stay into the loop until we have the desired numer of annuncement
    while len(descriptions_list)<=10000:
        # we get the page contanining the list of announcements
        url = r'https://www.immobiliare.it/vendita-case/roma/?criterio=rilevanza&pag='+str(page_number)
        soup = bs4.BeautifulSoup(requests.get(url).text)
        
        # we scarp the section contaning the features of the announcement
        other_data = soup.findAll("ul", {"class": "listing-features list-piped"})
        list_features_all = []
    
        # we place the feature one by one in a list. If all our tries fails, we place a 0 instead
        for k in other_data:
            list_features = []
            for i in k.find_all('li')[:5]:
                isinside = False
                try:
                    list_features.append(int(i.div.span.string[0]))
                    isinside = True
                except:
                    try:
                        list_features.append(int(i.abbr.text[0]))
                        isinside = True
                    except:
                        try:
                            y = i.string
                            y = int(''.join(re.findall('\d+',y)))
                            list_features.append(y)
                            isinside = True
                        except:
                            pass
                if not isinside:
                    list_features.append(0)
            # we check if we get the list correctly
            if len(list_features) == 5:
                list_features_all.append(list_features)
            # if not, we write it so we can skip this announcement for this page
            else:
                list_features_all.append('Not good')
    
        # now we scrap the part to find the description
        links = soup.findAll("p", {"class": "titolo text-primary"})
        
        for i in range(len(links)):
            # for each link we check if we get his features right
            if not list_features_all[i] == 'Not good':
                # if so we open the link
                link = links[i].a["href"]
                page_soup = bs4.BeautifulSoup(requests.get(link).text)
                # and get the description
                try:
                    description = page_soup.findAll("div", {"class":"col-xs-12 description-text text-compressed"})[0].text
                except IndexError:
                    description = None
                if description != None:
                    descriptions_list.append(str(description))
                # if the page had no description we place a "NaN" instead
                else:
                    descriptions_list.append('NaN')
                # we append in a new list also the features, in this way we exclude the 'Not good' annuncements
                list_features_all_c.append(list_features_all[i])
        page_number += 1
        time.sleep(0.8)
        
    return(descriptions_list,list_features_all_c)