def mostCommon(lst):
    return max(set(lst), key=lst.count)


def findSubset(X, Y):
    locations = []
    for i in range(len(X) - len(Y) + 1):
        if X == Y[i:i+len(X)]: locations.append(i)
    return locations