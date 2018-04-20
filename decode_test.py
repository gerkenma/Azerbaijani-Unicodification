from unidecode import unidecode
import unicodecsv
import codecs
from helper_functions import vocabulary
from helper_functions import helperFunctions

azj = open("azj-train.txt", "r", encoding="utf-8").read()
rawDict = {}
for letter in azj:
    rawDict[unidecode(letter)] = letter

helperFunctions.writeDictionary(rawDict, "rawDict.csv")
# rawDict = helperFunctions.readDictionary("rawDict.csv")
unfindable = {}
with open("input.csv", "r", encoding="UTF-8") as test:
    data = test.read()
    guessCsv = open("dictionaries\guessLetter.csv", "wb")
    writer = unicodecsv.writer(guessCsv)
    guessLetter = {}
    for letter in data:
        try:
            guessLetter[letter] = rawDict[letter]
            writer.writerow([guessLetter[letter], letter])
        except KeyError:
            unfindable[letter] = unidecode(letter)

print(unfindable)



# helperFunctions.writeDictionary(guessLetter, "guessLetter.csv")