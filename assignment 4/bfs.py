import urllib.request as rq
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# url = input('Enter link ')
# repeat = input('Enter breadth ')

wordsDictionary = dict()

urllist = list()

def getLinks(link):
    html = rq.urlopen(link).read()
    soup = BeautifulSoup(html,"lxml")
    tags = soup('a')
    for tag in tags:
        urllist.append(tag.get('href'))

def get_p_tags(link):
    html = rq.urlopen(link).read()
    soup = BeautifulSoup(html, "lxml")
    tags = soup.findAll('p')
    for tag in tags:
        p = tag.text
        # print(type(p))
        m = p.strip('. : / = ')
        m = m.lower()
        # print(m.split())
        append_words(m.split())

def append_words(words):
    for word in words:
        wordsDictionary[word] = wordsDictionary.get(word, 0) + 1


def plot_graph(wordsDictionary):
    frequentWords = {k: v for (k, v) in wordsDictionary.items() if v > 0}
    plt.bar(range(len(frequentWords)), frequentWords.values())
    plt.xticks(range(len(frequentWords)), frequentWords.keys(), rotation=-60)
    plt.title('Histogram of Frequency of words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()




get_p_tags('http://www.strathmore.edu/')
plot_graph(wordsDictionary)

# print(wordsDictionary)
#
# print(urllist)