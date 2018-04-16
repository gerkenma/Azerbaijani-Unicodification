from unidecode import unidecode

threeLetter = {}
fourLetter = {}
fiveLetter = {}


def buildMultiLetter():
    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        line = training.readline()
        for line in training:
            line = line.rstrip()

            for i in range(0, len(line) - 2):
                for j in range(i+3, min(len(line)+1, i+6)):
                    if len(line[i:j]) == 3:
                        threeLetter[unidecode(line[i:j]).replace("@", "e")] = line[i:j]

                    elif len(line[i:j]) == 4:
                        fourLetter[unidecode(line[i:j]).replace("@", "e")] = line[i:j]

                    else:
                        fiveLetter[unidecode(line[i:j]).replace("@", "e")] = line[i:j]

    return threeLetter, fourLetter, fiveLetter


def testMultiLetter(word, threeL, fourL, fiveL):
    upperFlag = not word == word.lower()
    word = word.lower()

    if not upperFlag:
        for i in range(0, len(word) - 2):
            for j in range(i+3, min(len(word)+1, i+6)):
                if len(word[i:j]) == 5:
                    try:
                        return word.replace(word[i:j], fiveL[word[i:j]])
                    except KeyError:
                        pass

                elif len(word[i:j]) == 4:
                    try:
                        return word.replace(word[i:j], fourL[word[i:j]])
                    except KeyError:
                        pass

                else:
                    try:
                        return word.replace(word[i:j], threeL[word[i:j]])
                    except KeyError:
                        pass
        return None

    else:
        for i in range(0, len(word) - 2):
            for j in range(i+3, min(len(word)+1, i+6)):
                if len(word[i:j]) == 5:
                    try:
                        return word.replace(word[i:j], fiveL[word[i:j]].capitalize())
                    except KeyError:
                        pass

                elif len(word[i:j]) == 4:
                    try:
                        return word.replace(word[i:j], fourL[word[i:j]].capitalize())
                    except KeyError:
                        pass

                else:
                    try:
                        return word.replace(word[i:j], threeL[word[i:j]].capitalize())
                    except KeyError:
                        pass
        return None