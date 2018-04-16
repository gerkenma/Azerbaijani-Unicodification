from helper_functions import testContext
from helper_functions import vocabulary
from helper_functions import letterFreq
from helper_functions import multiLetter
from helper_functions import helperFunctions

# wordList = testContext.buildWordList()
try:
    wordSet = helperFunctions.readDictionary("vocabulary.csv")
except FileNotFoundError:
    wordSet = vocabulary.buildVocabulary()
try:
    wordSet = helperFunctions.readDictionary("vocabulary.csv")
except FileNotFoundError:
    vocabulary.buildVocabulary()
    wordSet = helperFunctions.readDictionary("vocabulary.csv")

try:
    threeLetter = helperFunctions.readDictionary("threeLetter.csv")
    fourLetter = helperFunctions.readDictionary("fourLetter.csv")
    fiveLetter = helperFunctions.readDictionary("fiveLetter.csv")
except FileNotFoundError:
    multiLetter.buildMultiLetter()
    threeLetter = helperFunctions.readDictionary("threeLetter.csv")
    fourLetter = helperFunctions.readDictionary("fourLetter.csv")
    fiveLetter = helperFunctions.readDictionary("fiveLetter.csv")

try:
    freqList = helperFunctions.readDictionary("letterFreq.csv")
except FileNotFoundError:
    letterFreq.buildLetterFreq()
    freqList = helperFunctions.readDictionary("letterFreq.csv")

with open("input.csv", "r", encoding="UTF-8") as test:
    i = 0
    predictions = {}
    test.readline()
    eof = False
    wordsFound = 0

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
            if predictions[i] is not None: wordsFound += 1

        if predictions[i] is None:
            predictions[i] = letterFreq.testLetterFreq(line3, freqList)
            multiLetterEval = multiLetter.testMultiLetter(predictions[i], threeLetter, fourLetter, fiveLetter)
            if multiLetterEval is not None:
                wordsFound += 1
            predictions[i] = multiLetterEval

        line1 = line2
        line2 = line3
        line3 = test.readline()
        eof = not line3


print("Found ", wordsFound, " out of ", i)
helperFunctions.writeDictionary(predictions, "prediction.csv")
print("Output file successfully written.")