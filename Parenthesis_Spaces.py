stringA = '( ()) ((()()())) (()) ()'
stringB = '())((()())) (()((() ((()'
stringC = '(()()()))())) (()) (()()'


def seperateparenthesis(string):
    plist = []
    for i in string.replace(' ', ''):
        plist.append(i)
    print(plist)


seperateparenthesis(stringA)
seperateparenthesis(stringB)
seperateparenthesis(stringC)
