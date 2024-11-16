import data

a = [1, 2, 2, 2, 1, 1, 1, 1, 2]


def check_complex(seq=[]):
    w = [1, 1, 1]
    l = [2, 2, 2]

    h = data.h_data(seq)
    v = data.v_data(seq)
    d = [data.d_data(seq),data.rd_data(seq)]
    all = [h, v, d]
    temp = []

    for i in all:
        if w in i :
            if l in i:
                temp.append(2)
            else:
                temp.append(1)
        elif l in i:
            temp.append(0)
        elif (w not in i) and (l not in i):
            temp.append(-1)
    return max(temp)


