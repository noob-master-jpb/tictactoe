import data

a = [['O', 'X', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]


def board_num(lis):
    temp = []
    lis = lis[0] + lis[1] + lis[2]
    for i in lis:
        if i == 'O':
            temp.append(2)
        elif i == 'X':
            temp.append(1)
        elif i =='-':
            temp.append(0)

    return temp


def num_board(lis):
    lis = data.combine(lis)
    temp = []
    for i in lis:
        if i == 2:
            temp.append('O')
        elif i == 1:
            temp.append('X')
        elif i == 0:
            temp.append('-')
    return show_no_print(temp)


sep = [3, 4, 5, 6, 2]


def seq_num(lis):
    temp = [0 for i in range(9)]
    c = 1
    for i in lis:
        temp[i - 1] = c
        if c == 1:
            c = 2
        elif c == 2:
            c = 1
    return temp

def alternate_board(se= []):
    seq = list(se)
    temp = []
    for i in seq:
        if i == 1:
            temp.append(2)
        elif i == 2:
            temp.append(1)
        elif i == 0:
            temp.append(0)
        else:
            print("check for errors in sequence(0,1,2 are only valid)")
    return temp

def show_no_print(seq):
    temp = []
    for i in range(0, 9, 3):
        temp.append(seq[i:i + 3])
    return temp