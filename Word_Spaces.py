sentenceA = 'Python snakes kill,'
sentenceB = 'The Python coding language'
sentenceC = 'Does worse'


def seperatewords(sentence):
    listspacers = []
    listwords = []
    listedsentence = list(sentence)
    for word in listedsentence:
        if word == ',' or word == ' ':
            listspacers.append(word)
        else:
            listwords.append(word)
    print(listspacers)
    print(listwords)


seperatewords(sentenceA)
seperatewords(sentenceB)
seperatewords(sentenceC)
