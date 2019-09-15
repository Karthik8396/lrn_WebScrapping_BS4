

import bs4 as bs
from urllib import request
import urllib3
import os.path
import time
import feedparser

#start_time = time.time()
##TO DO GO TO PAGE ADD ?page=2 in the URL to continue downloading the pages .You will get the new RSS Feed XML with new contents

#SCRAPPING IS DONE BY RSS FEED
# FEEDPARSER MODULE IS USED TO PARSE THE XML RSS


# count=3  #limiting the number of downloads
# flag=0
image_links=[]
http = urllib3.PoolManager()
req = http.request('GET','https://old.reddit.com/r/all/.rss',headers = { 'User-Agent' : 'Mozilla/5.0' })
# #setting the header to make the site think the request came from the browser
sauce=req.data.decode('utf-8')   #decoding the response

fd=feedparser.parse(sauce)  #parsing the xml file 


req.release_conn()
entry=fd.get('entries')  #json file is retured after parsing and values can be accessed by get function
#print(entry)
for i in entry:
    html = bs.BeautifulSoup(i.content[0].value, 'html.parser')
    a=html.find_all('a')
    for i in a:

        if i.text=='[link]' and 'old.reddit.com' not in i.get('href') :
            image_links.append(i.get('href'))
            print(i.get('href'))                                            #getting all content links from the reddit page
print(len(image_links))                                                     
