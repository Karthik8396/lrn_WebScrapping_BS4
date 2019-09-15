import bs4 as bs
from urllib import request
import urllib3
import os.path
import time

start_time = time.time()
##TO DO GO TO PAGE ADD ?page=2 in the URL to continue downloading the pages .You will get the new RSS Feed XML with new contents


count=3  #limiting the number of downloads
flag=0
image_links=[]
http = urllib3.PoolManager()
req = http.request('GET','https://old.reddit.com/r/wallpapers/.rss',headers = { 'User-Agent' : 'Mozilla/5.0' })
#setting the header to make the site think the request came from the browser
sauce=req.data.decode('utf-8')   #decoding the response
req.close()
p=[]
soup=bs.BeautifulSoup(sauce,'xml')   # Parsing the xml rss feed
l=soup.find_all('content')
for i in l:
    p.append(i.text)
    flag=flag+1
    if flag==count:
        break


for j in p:
    html=bs.BeautifulSoup(j,'html.parser')
    a=html.find_all('a')
    for i in a:
        link = i.get('href')
        if "i.redd.it" in link:
            print('adding: '+str(link))
            image_links.append(link)

images=image_links
print("Retrived  "+ str(len(images)) + " images...")
print("Donwloading Images........")

for i in range(0,len(images)):
    p = images[i].split('/')
    fname=p[len(p)-1]
    if os.path.exists(fname):
        print("Skipping "+images[i]+' as '+fname+"  already exists")
    else:
        print("Downloading "+images[i]+' .......')
        f = open(fname, 'wb')    #writing the respose in file
        f.write(request.urlopen(images[i]).read())
        f.close()

print('Download Complete!!')

print("--- %s seconds ---" % (time.time() - start_time))