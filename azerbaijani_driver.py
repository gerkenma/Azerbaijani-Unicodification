from helper_functions import vocabulary
from helper_functions import letterFreq
from helper_functions import multiLetter
from helper_functions import helperFunctions
import re

# All training data is saved to files for faster processing
# Create dictionary of seen words
try:
    wordSet = helperFunctions.readDictionary("vocabulary.csv")
except FileNotFoundError:
    vocabulary.buildVocabulary()
    wordSet = helperFunctions.readDictionary("vocabulary.csv")

# Creates dictionary of seen 5/4/3 letter patterns
try:
    threeLetter = helperFunctions.readDictionary("threeLetter.csv")
    fourLetter = helperFunctions.readDictionary("fourLetter.csv")
    fiveLetter = helperFunctions.readDictionary("fiveLetter.csv")
except FileNotFoundError:
    multiLetter.buildMultiLetter()
    threeLetter = helperFunctions.readDictionary("threeLetter.csv")
    fourLetter = helperFunctions.readDictionary("fourLetter.csv")
    fiveLetter = helperFunctions.readDictionary("fiveLetter.csv")

# Creates dictionary of most frequently seen letter equivalents
try:
    freqList = helperFunctions.readDictionary("letterFreq.csv")
except FileNotFoundError:
    letterFreq.buildLetterFreq()
    freqList = helperFunctions.readDictionary("letterFreq.csv")

# Begins testing
with open("input.csv", "r", encoding="UTF-8") as test:
    i = 0
    predictions = {}
    test.readline()
    vocabCount = 0
    multiLetterCount = 0

    for line in test:
        i += 1
        line = re.split('[0-9]+,', line)[1].strip().replace('"', '')

        predictions[i], found = vocabulary.testVocabulary(line, wordSet)
        if found: vocabCount += 1

        if not found:
            predictions[i], found = multiLetter.testMultiLetter(predictions[i], threeLetter, fourLetter, fiveLetter)
            if found: multiLetterCount += 1
            predictions[i] = letterFreq.testLetterFreq(line, freqList)

        if i >= 100: break

helperFunctions.writeDictionary(predictions, "prediction.csv")
print("Output file successfully written.")
print("Total words:", i)
print("Vocab Words:", vocabCount)
print("multiLetter:", multiLetterCount)