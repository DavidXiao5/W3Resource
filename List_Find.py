listA = [19, 19, 5, 3, 5, 5, 3, 5, 0]
listB = [19, 12, 23, 345, 3]
listC = [35, 56, 55]


def findnums(used_list):
    return used_list.count(19) == 2 and used_list.count(5) >= 3


print(findnums(listA))
print(findnums(listB))
print(findnums(listC))
