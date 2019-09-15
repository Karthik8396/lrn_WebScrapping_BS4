import bs4 as bs
from urllib import request
import urllib3
import os.path
import time

start_time = time.time()

#to go to the next page add '?count=25&after=t3_d2zix0' and continue the same process for each page

count=3                                     #to limit the number of donwloads
flag=0
image_links=[]                              #stroing the image links
http = urllib3.PoolManager()                #http connection pool
req = http.request('GET','https://old.reddit.com/r/wallpapers/',headers = { 'User-Agent' : 'Mozilla/5.0' }) #setting the header to make the site think the request came from the browser

sauce=req.data.decode('utf-8')      # decoding the response in utf=8 format
req.release_conn()                         #request close
soup=bs.BeautifulSoup(sauce,'lxml')     #parsing the response
divs=soup.find_all('div',class_='content')
images=[]
for div in divs:
    urls=div.find_all('a')
    for url in urls:
        href=url.get('href')
        if  "/comments/" in href and "https://" in href :
            image_links.append(href)
            flag =flag+1
            if flag == count:
                break


#
# link = image_links[0]
# img_req=http.request('GET',link,headers = { 'User-Agent' : 'Mozilla/5.0' })
# data=img_req.data.decode('utf-8')
# img_req.close()
# img_soup=bs.BeautifulSoup(data,'lxml')
# l=img_soup.body.find_all('a',class_='title may-blank outbound')
# l=l[0].get('data-href-url')
# images.append(l)
# print(l)
#



for link in image_links:
    flag = +1
    if flag == count:
        break
    img_req=http.request('GET',link,headers = { 'User-Agent' : 'Mozilla/5.0' })
    data=img_req.data.decode('utf-8')
    img_req.close()
    img_soup=bs.BeautifulSoup(data,'lxml')
    l=img_soup.body.find_all('a',class_='title may-blank outbound')
    l=l[0].get('data-href-url')
    print("adding: " + l)
    images.append(l)

print("Retrived  "+ str(len(images)) + " images...")
print("Donwloading Images........")

for i in range(0,len(images)):
    p = images[i].split('/')
    fname=p[len(p)-1]
    if os.path.exists(fname):
        print("Skipping "+images[i]+' as '+fname+"  already exists")
    else:
        print("Downloading "+images[i]+' .......')
        f = open(fname, 'wb')                                               #Writing the response in the file as saving the file
        f.write(request.urlopen(images[i]).read())
        f.close()

print('Download Complete!!')

print("--- %s seconds ---" % (time.time() - start_time))