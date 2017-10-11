import matplotlib.pyplot as plt


wordsDictionary = dict()

file = open('alice.txt','r')
fileHandler = file.readlines()

for lines in fileHandler:
    for words in lines.split():
        word = words.lower()
        word = word.strip('.()",“ ')
        wordsDictionary[word] = wordsDictionary.get(word, 0) + 1

m = sorted(wordsDictionary.items(),key=lambda x:x[1],reverse=True)

frequentWords = {k:v for (k,v) in wordsDictionary.items() if v > 80}
#
print(list(frequentWords.values()))
n, bins, patches = plt.hist(list(frequentWords.values()))
# plt.bar(range(len(frequentWords)), frequentWords.values(), align='center')
# plt.xticks(range(len(frequentWords)), frequentWords.keys(),rotation=-60)
plt.title('Histogram of Frequency of words')
plt.xlabel('Words')
plt.ylabel('Frequency')

plt.show()


