import unicodecsv

def mostCommon(lst):
    return max(set(lst), key=lst.count)


def findSubset(X, Y):
    locations = []
    for i in range(len(X) - len(Y) + 1):
        if X == Y[i:i+len(X)]: locations.append(i)
    return locations


def getCapArray(word):
    capArray = []
    for letter in word:
        if letter.isupper():
            capArray.append(1)
        else:
            capArray.append(0)
    return capArray


def writeDictionary(dict, name):
    with open('dictionaries/' + name, 'wb') as output:
        writer = unicodecsv.writer(output)
        writer.writerow(["id", "token"])
        for key, value in dict.items():
            writer.writerow([key, value])


def readDictionary(name):
    dict = {}
    with open('dictionaries/' + name, 'r', encoding="UTF-8") as data:
        data.readline()
        for line in data:
            dict[line.split(",")[0]] = line.split(",")[1].rstrip().replace('"', '')

    return dict


if __name__ == "__main__":
    sample = readDictionary("sampleOut.csv")
    print(sample)
    writeDictionary(sample, "sample.csv")
