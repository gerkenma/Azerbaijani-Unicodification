from unidecode import unidecode
from helper_functions import helperFunctions

threeLetter = {}
fourLetter = {}
fiveLetter = {}


def buildMultiLetter():
    count = 0
    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        line = training.readline()

        for line in training:
            count += 1
            line = line.rstrip()

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

            if count >= 335:
                break

    for key in threeLetter:
        threeLetter[key] = helperFunctions.mostCommon(threeLetter[key])

    for key in fourLetter:
        fourLetter[key] = helperFunctions.mostCommon(fourLetter[key])

    for key in fiveLetter:
        fiveLetter[key] = helperFunctions.mostCommon(fiveLetter[key])

    return threeLetter, fourLetter, fiveLetter


def testMultiLetter(word, threeL, fourL, fiveL):
    length = 5
    replace = None

    capitalArray = helperFunctions.getCapArray(word)
    word = word.lower()

    while length >= 3:
        start = 0
        while start <= len(word) - length:
            end = start + length

            if len(word[start:end]) == 5:
                try:
                    replace = word.replace(word[start:end], fiveL[(word[start:end])])
                except KeyError:
                    pass

            elif len(word[start:end]) == 4:
                try:
                    replace = word.replace(word[start:end], fourL[(word[start:end])])
                except KeyError:
                    pass

            else:
                try:
                    replace = word.replace(word[start:end], threeL[(word[start:end])])
                except KeyError:
                    pass

            if replace is not None:
                capitalReplace = ""
                for i in range(len(capitalArray)):
                    if capitalArray[i] == 1:
                        capitalReplace += replace[i].upper()
                    else:
                        capitalReplace += replace[i]

                return capitalReplace


            start += 1
        length -= 1

    return None