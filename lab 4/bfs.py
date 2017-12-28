import urllib.request as rq
import matplotlib.pyplot as plt
import re
from collections import OrderedDict
import time



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
    sorted_dictionary = OrderedDict(sorted(wordsDictionary.items(), key=lambda v: v[1], reverse=True))
    most_frequent = {k: sorted_dictionary[k] for k in list(sorted_dictionary.keys())[:10]}
    # sorted_most_frequent = OrderedDict(sorted(most_frequent.items(), key=lambda v: v[1], reverse=True))
    plt.bar(range(len(most_frequent)), most_frequent.values())
    plt.xticks(range(len(most_frequent)), most_frequent.keys(), rotation=-60)
    plt.title('Frequency of words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()


start_time = time.clock()
getLinks('http://www.strathmore.edu/')
get_p_tags(urllist)
print (time.clock() - start_time, "seconds")
plot_graph(wordsDictionary)
print (time.clock() - start_time, "seconds")

