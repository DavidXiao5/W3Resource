stringA = '( ()) ((() ( ) () ) )  ( ( ) )  (  ) '
stringB = '(( ) ) ( ( ( ) ())) (()())(()) ((()))'
stringC = '(()()( ) )((())) (() )   ( ( )    ())'


def seperateparenthesis(string):
    listp = []
    stringp = ""
    for s in string.replace(' ', ''):
        stringp += s
        if stringp.count("(") == stringp.count(")"):
            listp.append(stringp)
            stringp = ""
    print(listp)


seperateparenthesis(stringA)
seperateparenthesis(stringB)
seperateparenthesis(stringC)
