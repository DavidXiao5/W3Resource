listA = [1, 1, 1, 1, 1]
listB = [2, 23, 23, 2, 4, 5]
listC = [2, 0, 1, 1, 3, 0, 0]


def findsumandlength(usedlist, i):
    return sum(usedlist[:i]) == i


print(findsumandlength(listA, 5))
print(findsumandlength(listB, 4))
print(findsumandlength(listC, 3))
