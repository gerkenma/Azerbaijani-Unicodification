from unidecode import unidecode
from helper_functions import helperFunctions

# Function adds all seen words to dictionary. Will keep most common seen variant of that word.


def buildVocabulary():
    vocab = {}

    with open("azj-train.txt", "r", encoding="UTF-8") as training:
        for line in training:
            line = line.lower().strip()
            try:
                vocab[unidecode(line).replace("@", "e")].append(line)
            except KeyError:
                vocab[unidecode(line).replace("@", "e")] = [line]

    for key in vocab:
        if len(vocab[key]) >= 2:
            vocab[key] = helperFunctions.mostCommon(vocab[key])
        else:
            vocab[key] = vocab[key][0]

    helperFunctions.writeDictionary(vocab, "vocabulary.csv")


def testVocabulary(word, vocab):
    upperFlag = not word.lower() == word

    if word in vocab:
        if upperFlag:
            return vocab[word].capitalize(), True
        else:
            return vocab[word], True
    else:
        return word, False
