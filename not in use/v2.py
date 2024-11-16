import random

a = [1,2,3,4,5,6,7,8,9]
b = [0 for j in range(9)]


def make(seq):
    n = int(input('----'))
    if (n<=9) and (n>=1):
        seq[n-1] = 1
    show(seq)


def show(seq):
    for i in range(0, 9, 3):
        print(seq[i:i + 3])


def display(seq):
    for i in seq:
        print(i)


def check(data):
    ctrl = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    if data in ctrl:
        ind = data.index(0)
        data[ind]= 2
    return data


# Horizontal zone---------------------
def h_data(seq):
    hstore = []
    for i in range(0, 9, 3):
        t = seq[i:i+3]
        hstore.append(t)
    return hstore


def h_check(seq):
    hc = h_data(seq)
    for i in hc:
        ind = hc.index(i)
        temp = check(i)
        hc[ind] = temp
    return hc


def h_ins(seq):
    seq = h_check(seq)
    lin = seq[0] + seq[1] + seq[2]
    return lin

# vertical zone----------------------
def v_data(seq):
    vstore = []
    for i in range(0,3):
        temp = []
        for j in range(0,9,3):
            t = seq[j+i]
            temp.append(t)
        vstore.append(temp)
    return vstore


def v_check(seq):
    vc = v_data(seq)
    for i in vc:
        ind = vc.index(i)
        temp = check(i)
        vc[ind] = temp
    return vc


def v_ins(seq):
    dat = seq
    vi = v_check(dat)
    lim = []
    for i in range(0,3):
        for item in vi:
            lim.append(item[i])
    return lim


# diagonal zone ---------------------
def d_data(seq):
    dstore = []
    for i in range(0,9,4):
        dstore.append(seq[i])
    return dstore


def d_check(seq):
    dc = check(d_data(seq))
    return dc


def d_ins(seq,data):
    count = 0
    back = seq
    for i in range(0,9,4):
        back[i] = data[count]
        count += 1
    return back


# reverse diagonal zone-------------
def rd_data(seq):
    rdstore = []
    for j in range(2,7,2):
        rdstore.append(seq[j])
    return rdstore


def rd_check(seq):
    rc = check(rd_data(seq))
    return rc


def rd_ins(seq,data):
    count = 0
    back = seq
    for i in range(2,7,2):
        back[i] = data[count]
        count += 1
    return back


def defend(seq):
    dif = tuple(seq)
    temp = []
    final = []
    while True:
        h = h_ins(list(dif))
        temp.append(h)
        v = v_ins(list(dif))
        temp.append(v)
        d = d_ins(list(dif), d_check(list(dif)))
        temp.append(d)
        rd = rd_ins(list(dif), rd_check(list(dif)))
        temp.append(rd)
        break


    for item in temp:
        if item != list(dif):
            final.append(item)
    if final != []:
        out = random.choice(final)
        return list(out)
    else:
        return list(dif)

def no():
    h = h_ins(b)
    v = v_ins(b)
    d = d_ins(b, d_check(b))
    rd = rd_ins(b, rd_check(b))
    print(h)
    print(v)
    print(d)
    print(rd)


while True:
    make(b)
    b = defend(b)
    show(b)
