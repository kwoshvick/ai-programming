import urllib.request as rq
import matplotlib.pyplot as plt
import re
from collections import OrderedDict



wordsDictionary = dict()
urllist = list()
mostfrequent = OrderedDict()

def getLinks(link):
    html = rq.urlopen(link).read()
    html = str(html)
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
    i = ' '.join(urls)
    links = i.split()
    for link in links:
        if link == '\\,':
            continue
        if link == '\\':
            continue
        urllist.append(link)

def get_p_tags(urls):
    for link in urls:
        try:
            html = rq.urlopen(link).read()
            html = str(html)
            m = re.findall(r'<p>([^]]+)</p>', html)
            for i in m:
                n = i.strip('. <p> </p> ')
                for y in n.split():
                    y2 = y.lower()
                    wordsDictionary[y2] = wordsDictionary.get(y2, 0) + 1
        except :
            continue



def plot_graph(wordsDictionary):
    average = sum(wordsDictionary.values())/len(wordsDictionary.values())
    frequentWords = {k: v for (k, v) in wordsDictionary.items() if v > average-1}
    plt.bar(range(len(frequentWords)), frequentWords.values())
    plt.xticks(range(len(frequentWords)), frequentWords.keys(), rotation=-60)
    plt.title('Histogram of Frequency of words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()



getLinks('http://www.strathmore.edu/')
get_p_tags(urllist)
plot_graph(wordsDictionary)
