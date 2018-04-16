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
