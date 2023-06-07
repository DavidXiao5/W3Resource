listA = [19, 19, 5, 3, 5, 5, 3, 5]
listB = [19, 12, 23, 345, 3, 3, 3]
listC = [35, 56, 55, 2, 2, 5, 2, 5]


def findcountnums(used_list):
    return len(used_list) == 8 and used_list.count(used_list[4]) >= 3


print(findcountnums(listA))
print(findcountnums(listB))
print(findcountnums(listC))
