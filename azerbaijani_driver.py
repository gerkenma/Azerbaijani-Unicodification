import unicodecsv
from helper_functions import testContext
from helper_functions import vocabulary
from helper_functions import letterFreq
from helper_functions import multiLetter

# wordList = testContext.buildWordList()
wordSet = vocabulary.buildVocabulary()
threeLetter, fourLetter, fiveLetter = multiLetter.buildMultiLetter()
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

        predictions[i] = testContext.threeLineContext()

        if predictions[i] is None:
            predictions[i] = testContext.twoLineContext()

        if predictions[i] is None:
            predictions[i] = vocabulary.testVocabulary(line3, wordSet)

        if predictions[i] is None:
            predictions[i] = multiLetter.testMultiLetter(line3, threeLetter, fourLetter, fiveLetter)

        if predictions[i] is None:
            predictions[i] = letterFreq.testLetterFreq(line3, freqList)
            if predictions[i] is not None:
                predictions[i] = letterFreq.testLetterFreq(predictions[i], freqList)
            else:
                predictions[i] = letterFreq.testLetterFreq(line3, freqList)
                wordsNotFound += 1

        line1 = line2
        line2 = line3
        line3 = test.readline()
        eof = not line3


print("Found ", i-wordsNotFound, " out of ", i)
with open('prediction.csv', 'wb') as output:
    writer = unicodecsv.writer(output)
    writer.writerow(["id", "token"])
    for key,value in predictions.items():
        writer.writerow([key, value])
    print("Output file successfully written.")