from unidecode import unidecode
from helper_functions import helperFunctions


def buildLetterFreq():
    letterList = {}
    letterFreq = {}

    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        for word in training:
            word = word.rstrip()
            if word.isalpha():
                for letter in word:
                    try:
                        letterList[unidecode(letter).lower().replace("@", "e")].append(letter.lower())
                    except KeyError:
                        letterList[unidecode(letter).lower().replace("@", "e")] = [letter.lower()]

    for item in letterList:
        letterFreq[item] = helperFunctions.mostCommon(letterList[item])

    return letterFreq

def testLetterFreq(word, freqList):
    # Unicode characters that resolve to be two or more ASCII characters
    comboLetters = ["kh", "ae", "ts", "ss", "ia", "dj", "fi", "sh", "s'", "y'", "ng", "dzh"]

    for combo in comboLetters:
        if word.lower() == word:
            if combo in word:
                word = word.replace(combo, freqList[combo])
        else:
            if combo in word.lower():
                word = word.replace(combo, freqList[combo].upper())

    guess = ""
    for letter in word:
        upperFlag = letter.isupper()

        if letter in freqList:
            guess += freqList[letter]
        else:
            guess += letter

        if upperFlag:
            guess = guess[0:len(guess)-1] + guess[len(guess)-1].upper()

    return guess

