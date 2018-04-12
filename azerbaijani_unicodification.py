import unidecode
import unicodecsv

training = {}
asciiTrain = {}


def mostCommon(lst):
    return max(set(lst), key=lst.count)


def wordUnigramVote(inputWord):
    with open("azj-train.txt", "r", encoding="UTF-8") as data:
        for word in data:
            word = word.rstrip()
            if word.isalpha():
                try:
                    training[word] += 1
                except KeyError:
                    training[word] = 1

    for word in training:
        convert = unidecode.unidecode(word).replace("@", "e")
        asciiTrain[convert] = word


def letterUnigramVote(inputWord):
    with open("azj-train.txt", "r", encoding="UTF-8") as data:
        for word in data:
            word = word.rstrip()
            if word.isalpha():
                for letter in word:
                    try:
                        training[letter] += 1
                    except KeyError:
                        training[letter] = 1

    print(training)
    for letter in training:
        convert = unidecode.unidecode(letter).replace("@", "e")
        try:
            asciiTrain[convert].append((letter, training[letter]))
        except KeyError:
            asciiTrain[convert] = [(letter, training[letter])]

letterUnigramVote()
print(asciiTrain)
prediction = {}
with open("input.csv", "r", encoding="UTF-8") as test:
    test.readline()
    for line in test:
        word = line.split(",")[1].rstrip().replace('"', '')
        prediction[i] = ""

        for letter in word:
            if letter in asciiTrain:
                max = 0
                replace = "ERROR"
                for variant in asciiTrain[letter]:
                    if variant[1] > max:
                        max = variant[1]
                        replace = variant[0]
                prediction[i] += replace
            else:
                prediction[i] += letter

print(prediction)
with open('prediction.csv', 'wb') as output:
    writer = unicodecsv.writer(output)
    writer.writerow(["id", "token"])
    for key,value in prediction.items():
        writer.writerow([key, value])