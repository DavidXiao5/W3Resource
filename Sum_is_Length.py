listA = [1, 1, 1, 1, 1]
listB = [2, 23, 23, 2, 4, 5]
listC = [2, 0, 1, 1, 3, 0, 0]


def findsumandlength(usedlist):
    return len(usedlist) == sum(usedlist)


print(findsumandlength(listA))
print(findsumandlength(listB))
print(findsumandlength(listC))
