string_listA = ['hole', 'sdf', 'sdfef']
string_listB = ['efew', 'fef', 'efe']
string_listC = ['esd', 'vdd', 'efgjhvddrg']


def findsubstrings(stringlist):
    return stringlist[-2] in stringlist[-1]


print(findsubstrings(string_listA))
print(findsubstrings(string_listB))
print(findsubstrings(string_listC))
