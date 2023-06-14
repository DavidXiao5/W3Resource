listA = [1, 2, 3, 4, 5, 6, 7]
listB = [1, 2, 3, 3, 4, 4, 3]
listC = [1, 2, 3, 4, 3, 2, 1]


def findconsecutive(used_list):
    cnum = used_list[0]
    for num in used_list[1:-1]:
        if cnum != num:
            cnum = num
        else:
            return False
    if cnum != used_list[-1]:
        return True


print(findconsecutive(listA))
print(findconsecutive(listB))
print(findconsecutive(listC))
