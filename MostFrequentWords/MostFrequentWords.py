wordsList = []
wordsDictionary = {}
file = open("pantadeusz.txt", "r", encoding = "utf-8")

for line in file:
    wordsList.extend(line.lower().split())

file.close()

for i in range(len(wordsList)):
    wordsList[i] = wordsList[i].strip("\ufeff.!,()?:;/»«…")
    
    if len(wordsList[i]) >= 5:
        if wordsList[i] in wordsDictionary.keys():
            wordsDictionary[wordsList[i]] = wordsDictionary[wordsList[i]] + 1
        else:
            wordsDictionary[wordsList[i]] = 1

wordsSorted = sorted(wordsDictionary, key = wordsDictionary.get, reverse = True)

print("20 most frequent words in loaded file:\n")
for i in range (0, 20):
    print('%i. "%s" - %i occurences' % (i + 1, wordsSorted[i], wordsDictionary[wordsSorted[i]]))
