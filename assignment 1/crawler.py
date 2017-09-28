import urllib.request as rq
from bs4 import BeautifulSoup

url = input('Enter url (start https or http) : ')


html = rq.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))