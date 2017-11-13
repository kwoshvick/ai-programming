import urllib.request as rq
from bs4 import BeautifulSoup

url = input('Enter link ')
# repeat = input('Enter breadth ')



urllist = list()
last_link = list()

def getLinks(link):
    global soup
    global tags
    html = rq.urlopen(link).read()
    soup = BeautifulSoup(html,"lxml")
    tags = soup('a')
    for tag in tags:
        urllist.append(tag.get('href'))


getLinks(url)

print(urllist)