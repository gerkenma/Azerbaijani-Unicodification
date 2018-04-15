import unicodecsv
from helper_functions import testContext
from helper_functions import vocabulary
from helper_functions import letterFreq

# wordList = testContext.buildWordList()
wordSet = vocabulary.buildVocabulary()
freqList = letterFreq.buildLetterFreq()

with open("input.csv", "r", encoding="UTF-8") as test:
    i = 0
    predictions = {}
    test.readline()
    eof = False
    wordsNotFound = 0

    line1 = None
    line2 = None
    line3 = test.readline()

    while not eof:
        i += 1
        line3 = line3.split(",")[1].rstrip().replace('"', '')

        if line3.isalpha():
            predictions[i] = testContext.threeLineContext()

            if predictions[i] is None:
                predictions[i] = testContext.twoLineContext()

            if predictions[i] is None:
                predictions[i] = vocabulary.testVocabulary(line3, wordSet)

            if predictions[i] is None:
                wordsNotFound += 1
                predictions[i] = letterFreq.testLetterFreq(line3, freqList)

        else:
            predictions[i] = line3

        line1 = line2
        line2 = line3
        line3 = test.readline()
        eof = not line3

print(wordSet)
print(predictions)
print("Found ", i-wordsNotFound, " out of ", i)
with open('prediction.csv', 'wb') as output:
    writer = unicodecsv.writer(output)
    writer.writerow(["id", "token"])
    for key,value in predictions.items():
        writer.writerow([key, value])
    print("Output file successfully written.")