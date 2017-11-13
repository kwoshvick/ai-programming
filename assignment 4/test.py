import urllib.request as rq
from bs4 import BeautifulSoup

wordsDictionary = dict()
link = "http://www.strathmore.edu/"
f = rq.urlopen(link).read()
# myfile = f.read()
# print (myfile)
# content = urllib2.urlopen(url).read()

soup = BeautifulSoup(f,"lxml")
soup = str(soup)
soup = soup.split()

for i in soup:
    # print(i)
    # print("----")
    wordsDictionary[i] = wordsDictionary.get(i, 0) + 1

print (wordsDictionary)