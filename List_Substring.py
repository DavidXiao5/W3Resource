string_listA = ['hole', 'sdf', 'sdfef']
string_listB = ['efew', 'fef', 'efe']
string_listC = ['esd', 'vdd', 'efgjhvddrg']
string_listD = ['efg', 'ejrg', 'ejrg']


def findsubstrings(stringlist):
    return stringlist[-2] in stringlist[-1] and stringlist[-2] != stringlist[-1]


print(findsubstrings(string_listA))
print(findsubstrings(string_listB))
print(findsubstrings(string_listC))
print(findsubstrings(string_listD))