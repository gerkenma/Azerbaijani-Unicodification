from unidecode import unidecode
from helper_functions import helperFunctions

# Function finds every five, four, and three letter combination
# Combos are first added to a set
# After all training has completed, each dictionary key's set
# is reduced to the single most prevalent combo associated
# wit that key


def buildMultiLetter():
    threeLetter = {}
    fourLetter = {}
    fiveLetter = {}
    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        for line in training:
            line = line.strip()

            length = 5
            while length >= 3:
                start = 0
                while start <= len(line) - length:
                    end = start + length

                    if len(line[start:end]) == 3:
                        try:
                            threeLetter[unidecode(line[start:end]).replace("@", "e")].append(line[start:end])
                        except KeyError:
                            threeLetter[unidecode(line[start:end]).replace("@", "e")] = [(line[start:end])]

                    elif len(line[start:end]) == 4:
                        try:
                            fourLetter[unidecode(line[start:end]).replace("@", "e")].append(line[start:end])
                        except KeyError:
                            fourLetter[unidecode(line[start:end]).replace("@", "e")] = [(line[start:end])]

                    else:
                        try:
                            fiveLetter[unidecode(line[start:end]).replace("@", "e")].append(line[start:end])
                        except KeyError:
                            fiveLetter[unidecode(line[start:end]).replace("@", "e")] = [(line[start:end])]

                    start += 1
                length -= 1

    # Reduces each key's to single most common variant
    for key in threeLetter:
        threeLetter[key] = helperFunctions.mostCommon(threeLetter[key])

    for key in fourLetter:
        fourLetter[key] = helperFunctions.mostCommon(fourLetter[key])

    for key in fiveLetter:
        fiveLetter[key] = helperFunctions.mostCommon(fiveLetter[key])

    helperFunctions.writeDictionary(threeLetter, "threeLetter.csv")
    helperFunctions.writeDictionary(fourLetter, "fourLetter.csv")
    helperFunctions.writeDictionary(fiveLetter, "fiveLetter.csv")


def testMultiLetter(word, threeL, fourL, fiveL):
    length = 5
    replace = None

    orig = word
    word = word.lower()
    changes = 0
    while length >= 3:
        temp = word
        start = 0
        found = False
        while start <= len(word) - length:
            end = start + length

            if len(word[start:end]) == 5:
                try:
                    word = word.replace(word[start:end], fiveL[(word[start:end])])
                    print("Replaced", temp[start:end], "with", word[start:end])
                    changes += 1
                    found = True
                except KeyError:
                    pass

            elif len(word[start:end]) == 4:
                try:
                    word = word.replace(word[start:end], fourL[(word[start:end])])
                    print("Replaced", temp[start:end], "with", word[start:end])
                    changes += 1
                    found = True
                except KeyError:
                    pass

            else:
                try:
                    word = word.replace(word[start:end], threeL[(word[start:end])])
                    print("Replaced", temp[start:end], "with", word[start:end])
                    changes += 1
                    found = True
                except KeyError:
                    pass

            start += 1
        length -= 1
    print("Changes:", changes)
    return helperFunctions.fixCaps(orig, replace), found