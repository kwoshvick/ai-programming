import matplotlib.pyplot as plt


wordsDictionary = dict()

file = open('alice.txt','r')
fileHandler = file.readlines()

for lines in fileHandler:
    for words in lines.split():
        word = words.lower()
        word = word.strip('.()",“ ')
        wordsDictionary[word] = wordsDictionary.get(word, 0) + 1

frequentWords = {k:v for (k,v) in wordsDictionary.items() if v > 80}


# Plot histogram using matplotlib bar().
plt.bar(range(len(frequentWords)), frequentWords.values())
plt.xticks(range(len(frequentWords)), frequentWords.keys(),rotation=-60)
plt.title('Histogram of Frequency of words')
plt.xlabel('Words')
plt.ylabel('Frequency')

plt.show()


