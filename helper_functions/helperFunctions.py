import unicodecsv
import codecs


def mostCommon(lst):
    return max(set(lst), key=lst.count)


def findSubset(X, Y):
    locations = []
    for i in range(len(X) - len(Y) + 1):
        if X == Y[i:i+len(X)]: locations.append(i)
    return locations


def fixCaps(original, lower):
    if lower is None: return lower
    capArray = []
    for letter in original:
        if letter.isupper():
            capArray.append(1)
        else:
            capArray.append(0)

    reCapped = ""
    for i in range(len(lower)):
        if capArray[i] == 1:
            reCapped += lower[i].upper()
        else:
            reCapped += lower[i]

    return reCapped


def writeDictionary(dict, name):
    with open('dictionaries/' + name, 'wb') as output:
        writer = unicodecsv.writer(output)
        # quotes = False
        # if name == "prediction.csv":
        #     writer = unicodecsv.writer(output)
        #     writer.writerow(["id", "token"])
        #     writer = unicodecsv.writer(output, quoting=unicodecsv.QUOTE_NONNUMERIC)
        # else:
        #     writer = unicodecsv.writer(output)

        for key, value in dict.items():
            writer.writerow([key, value])



def readDictionary(name):
    dict = {}
    with open('dictionaries/' + name, 'r', encoding="UTF-8") as data:
        data.readline()
        for line in data:
            dict[line.split(",")[0]] = line.split(",")[1].strip().replace('"', '')

    return dict


def writeList(lst, name):
    output = codecs.open("lists/"+name, "wb", encoding="utf-8")
    for item in lst:
        output.write(item)
    output.close()


def readList(name):
    lst = []
    input = codecs.open("lists/"+name, "r", encoding="utf-8")
    lst = input.read()
    return lst

if __name__ == "__main__":
    orig = "hElLo!"
    word = "hello!"
    print(fixCaps(orig, word))