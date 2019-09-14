import bs4 as bs
import urllib.request
import pandas as pd

#sauce= urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()  #reading the html content
#soup=bs.BeautifulSoup(sauce,'lxml')                                                        #parsing the html content
#print(soup.find_all('p'))                                                                  #finds all paragraph tags <p>
#print(soup.find_all('p'))

#for para in soup.find_all('p'):                                                 #printing all p tags
 #   print(para.text)                                                            #.text gets text .string gives only values

#for url in soup.find_all('a'):                                                  #getting all <a> tags
 #   print(url.get('href'))                                                      # getting href attributes from <a>
#print(soup.nav)
#nav=soup.nav                                                                       # nav bar
#for url in nav.find_all('a'):
 #   print(url.get('href'))
#table=soup.table                                                               #getting table values
#tr=table.find_all('tr')
#for t_r in tr:
 #   td=t_r.find_all('td')
  #  row=[i.text for i in td]                                                               #converting table rows to arrays
   # print(row)

#print(table)

#dfs=pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)                     #pandas can be used to read table data in html files
#for df in dfs:
 #   print(df)                                                                                  #printing the table data


sauce= urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()  #reading the XML content
soup=bs.BeautifulSoup(sauce,'xml')                                                  #parsing XML
#print(soup)

for url in soup.find_all('loc'):                        #reading all urls from sitemap
    print(url.text)