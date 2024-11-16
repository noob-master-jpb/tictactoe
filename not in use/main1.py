a = [[0 for i in range(3)] for j in range(3)]

def trav(i):
    if i == 0:
        return 2
    elif i == 2:
        return 0
    else:
        return i

def show(list):
    for i in list:
        print(i)

def make(list):
    n = int(input('---'))

    row = (n // 10) - 1
    col = (n % 10) - 1

    if (row <= 3) and (col <= 3):
        list[row][col] = 1
        show(list)
        print('')
    else:
        print('invalid')

def hor(list):
    c = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    for sub in list:
        if sub in c:
            ind = sub.index(0)
            id = list.index(sub)
            list[id][ind] = 2

def vir(list):
    c = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]

    for ind in range(0,3):
        blank = []
        for i in list:
            j = int(i[ind])
            blank.append(j)
        if blank in c:
            o = blank.index(0)
            list[o][ind] = 2

def dig(list):
    c = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    blank = []
    z = 0
    for i in list:
        blank.append(i[z])
        z += 1
    if blank in c:
        ind = blank.index(0)
        list[ind][ind] = 2

def revdig(list):
    c = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    blank = []
    z = 2
    for i in list:
        blank.append(i[z])
        z -= 1
    if blank in c:
        ind = blank.index(0)
        list[ind][travdig(ind)] = 2

