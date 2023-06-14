listA = [1, 1, 1, 1, 123, 342, 234]
listB = [2, 23, 23, 2, 4, 5, 34, 3]
listC = [2, 0, 1, 1, 3, 0, 2, 23424, 324, 0]


def findnumsundernum(threshold, used_list):
    index = []
    time = 0
    for num in used_list:
        if num <= threshold:
            index.append(time)
        time += 1
    print(index)


findnumsundernum(150, listA)
findnumsundernum(10, listB)
findnumsundernum(5, listC)
