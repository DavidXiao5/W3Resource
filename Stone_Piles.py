nA = 3
nB = 10
nC = 42


def stone_piles(n):
    n_list = []
    for i in range(n):
        n_list.append(n)
        n += 2
    print(n_list)


stone_piles(nA)
stone_piles(nB)
stone_piles(nC)
