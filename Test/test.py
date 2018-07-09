#### ---- created ----   #####

import wikipedia
import requests
import json


# getting page id from url
title = 'తెలంగాణ'
url = 'http://te.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=' + title
resp = requests.get(url)
print(resp.status_code)  # 200
print(resp.json())


# getting page from wiki
wikipedia.set_lang('te')
ma = wikipedia.WikipediaPage(title=title)

with open('temp.txt', 'w', encoding='utf-8') as f:
    f.write(ma.links)

f = open('temp.txt', 'w', encoding='utf-8')
for link in ma.links:
    f.write(link)
    f.write('\n')
    

