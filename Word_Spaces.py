import re
sentenceA = 'Python snakes kill.'
sentenceB = 'The Python coding language...'
sentenceC = 'does worse'


def seperatewords(string):
    merged = re.split('([, ])', string)
    return [merged[::2], merged[1::2]]


print(seperatewords(sentenceA))
print(seperatewords(sentenceB))
print(seperatewords(sentenceC))
