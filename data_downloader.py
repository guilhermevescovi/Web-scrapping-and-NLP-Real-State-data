import requests
import bs4
import time
import re


def downloader():
    page_number = 1
    list_features_all_c = []
    descriptions_list = []
    
    while len(descriptions_list)<=10000:
        url = r'https://www.immobiliare.it/vendita-case/roma/?criterio=rilevanza&pag='+str(page_number)
        soup = bs4.BeautifulSoup(requests.get(url).text)
        
        
        other_data = soup.findAll("ul", {"class": "listing-features list-piped"})
        list_features_all = []
    
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
            if len(list_features) == 5:
                list_features_all.append(list_features)
            else:
                list_features_all.append('Not good')
    
        links = soup.findAll("p", {"class": "titolo text-primary"})
    
        for i in range(len(links)):
            if not list_features_all[i] == 'Not good':
                link = links[i].a["href"]
                page_soup = bs4.BeautifulSoup(requests.get(link).text)
                description = page_soup.findAll("div", {"class":"col-xs-12 description-text text-compressed"})[0].text
                if description != None:
                    descriptions_list.append(str(description))
                else:
                    descriptions_list.append('NaN')
                list_features_all_c.append(list_features_all[i])
        page_number += 1
        time.sleep(1)
        
    return(descriptions_list,list_features_all_c)