wordsDictionary = dict()

file = open('alice.txt','r')
fileHandler = file.readlines()

for lines in fileHandler:
    for words in lines.split():
        word = words.lower()
        word = word.strip('.()",“ ')
        wordsDictionary[word] = wordsDictionary.get(word, 0) + 1

print(sorted(wordsDictionary.items(),key=lambda x:x[1],reverse=True))


