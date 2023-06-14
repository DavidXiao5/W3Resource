listA = [1, 2, 3, 4, 5, 6, 7]
listB = [1, 2, 3, 3, 4, 4, 3]
listC = [1, 2, 3, 4, 3, 2, 1]
listD = [1, 11, 1, 11, 1, 11]


def findconsecutive(used_list):
    for num in range(len(used_list)-1):
        if used_list[num] == used_list[num+1]:
            return False
    return True


print(findconsecutive(listA))
print(findconsecutive(listB))
print(findconsecutive(listC))
print(findconsecutive(listD))
