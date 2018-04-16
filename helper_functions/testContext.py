# Code is functional but entirely too slow
# Currently (likely permanently) unused in program

# Embed the following code into the top of
# 'azjerbaijani_driver.py' to implement
#
# try:
#     rawList = helperFunctions.readList("rawList.csv")
#     decodedList = helperFunctions.readList("decodedList.csv")
# except FileNotFoundError:
#     testContext.buildContext()
#     rawList = helperFunctions.readList("rawList.txt")
#     decodedList = helperFunctions.readList("decodedList.txt")

# Embed the following code prior to the conditionals
# in 'azjerbaijani_driver.py' to implement
# predictions[i] = testContext.testThreeLineContext(line1, line2, word, rawList, decodedList)
# if predictions[i] is not None: wordsFound += 1
#
# if predictions[i] is None:
#     predictions[i] = testContext.testTwoLineContext(line2, word, rawList, decodedList)
#     if predictions[i] is not None: wordsFound += 1

from helper_functions import helperFunctions
from unidecode import unidecode


def buildContext():
    rawList = []
    decodedList = []

    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        for line in training:
            line = line.rstrip().replace('"', '')
            rawList.append(line)
            decodedList.append(unidecode(line).replace("@", "e"))

        helperFunctions.writeList(rawList, "rawList.txt")
        helperFunctions.writeList(decodedList, "decodedList.txt")


def testThreeLineContext(w1, w2, w3, raw, decoded):
    try:
        test = w1+w2+w3
    except TypeError:
        try:
            test = w2+w3
        except TypeError:
            test = w3

    for i in range(len(raw) - len(test) + 1):
        if test == decoded[i:i+len(test)]:
            return raw[i+len(test)-len(w3)+1:i+len(test)+1]

    return None


def testTwoLineContext(w1, w2, raw, decoded):
    try:
        test = w1+w2
    except TypeError:
        test = w2

    for i in range(len(raw) - len(test) + 1):
        if test == decoded[i:i+len(test)]:
            return raw[i+len(test)-len(w2)+1:i+len(test)+1]


    return None