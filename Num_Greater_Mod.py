numA = 922
numB = 934
numC = 344


def findnummod(num):
    return num > 4 ** 4 and num % 34 == 4


print(findnummod(numA))
print(findnummod(numB))
print(findnummod(numC))
