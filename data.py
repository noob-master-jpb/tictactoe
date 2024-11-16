import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0 for j in range(9)]

mid = [i for i in range(1, 8, 2)]
corners = [i for i in range(0, 10, 2) if i != 4]


# presentation and control zone


def make(seq,m = 3):
    bak = list(seq)
    n = int(input('----'))
    if (n <= 9) and (n >= 1):
        bak[n - 1] = m
    return bak
    # show(seq)


def combine(seq=[]):
    tem = []
    for i in seq:
        tem += i
    return tem


def show(seq):
    temp = []
    for i in range(0, 9, 3):
        print(seq[i:i + 3])
        temp.append(seq[i:i + 3])
    return temp



def display(seq):
    for i in seq:
        print(i)


def check(data):  # checks for two input in a row
    ctrl = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    if data in ctrl:
        ind = data.index(0)
        data[ind] = 2
    return data

    # -------------------- defending zone------------------ #


# data manipulation zone---------------------
def h_data(seq):
    hstore = []
    for i in range(0, 9, 3):
        t = seq[i:i + 3]
        hstore.append(t)
    return hstore


def v_data(seq):
    vstore = []
    for i in range(0, 3):
        temp = []
        for j in range(0, 9, 3):
            t = seq[j + i]
            temp.append(t)
        vstore.append(temp)
    return vstore


def d_data(seq):
    dstore = []
    for i in range(0, 9, 4):
        dstore.append(seq[i])
    return dstore


def rd_data(seq):
    rdstore = []
    for j in range(2, 7, 2):
        rdstore.append(seq[j])
    return rdstore


# check zone
def h_check(seq):
    hc = h_data(seq)
    for i in hc:
        ind = hc.index(i)
        temp = check(i)
        hc[ind] = temp
    return hc


def v_check(seq):
    vc = v_data(seq)
    for i in vc:
        ind = vc.index(i)
        temp = check(i)
        vc[ind] = temp
    return vc


def d_check(seq):
    dc = check(d_data(seq))
    return dc


def rd_check(seq):
    rc = check(rd_data(seq))
    return rc


# insertion zone
def h_ins(seq):
    seq = h_check(seq)
    lin = seq[0] + seq[1] + seq[2]
    return lin


def v_ins(seq):
    dat = seq
    vi = v_check(dat)
    lim = []
    for i in range(0, 3):
        for item in vi:
            lim.append(item[i])
    return lim


def d_ins(seq, data):
    count = 0
    back = seq
    for i in range(0, 9, 4):
        back[i] = data[count]
        count += 1
    return back


def rd_ins(seq, data):
    count = 0
    back = seq
    for i in range(2, 7, 2):
        back[i] = data[count]
        count += 1
    return back


# data control zone

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


def win(data):
    trl = [1, 1, 1]
    prl = [2, 2, 2]
    if (trl in data):  # or (prl in data):
        return True
    else:
        return False


def win_check(sep):
    # seq = indco(sep)
    h = win(h_data(sep))
    v = win(v_data(sep))
    d = win([d_data(sep), rd_data(sep)])
    ans = h or v or d
    return ans


cop = [i for i in range(1, 10)]


def indco(seq):
    temp = [''] * 9
    p = 1
    for i in seq:
        temp[int(i) - 1] = p
        if p == 1:
            p = 2
        else:
            p = 1
    return temp


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


def check_im_win(mat=[], mode=0):  # 0 for horizontal and 1 for vertical and 2 for diagonals and 3 for reverse diagonal
    ctrl = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    if mode == 0:
        for i in mat:
            i_id = mat.index(i)
            if i in ctrl:
                c_id = ctrl.index(i)
                return i_id * 3 + c_id
    if mode == 1:
        for i in mat:
            i_id = mat.index(i)
            if i in ctrl:
                c_id = ctrl.index(i)
                return c_id * 3 + i_id
    elif mode == 2:
        if mat in ctrl:
            return 4 * ctrl.index(mat)
    elif mode == 3:
        if mat in ctrl:
            return 2 * (ctrl.index(mat) + 1)


def im_win(seq):
    h = check_im_win(h_data(seq))
    v = check_im_win(v_data(seq),1)
    d = check_im_win(d_data(seq), 2)
    rd = check_im_win(rd_data(seq), 3)

    all = [h, v, d, rd]
    temp = []
    for i in all:
        if (i not in temp) and (i != None):
            temp.append(i)
    return temp


def check_complex(seq=[]):
    w = [1, 1, 1]
    l = [2, 2, 2]

    h = h_data(seq)
    v = v_data(seq)
    d = [d_data(seq), rd_data(seq)]
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

def step_check_complex(seq):
    for i in range(5, len(seq)+1):
        dat = seq[:i]
        if check_complex(seq_num(dat)) == -1:
            if i == 9:
                return check_complex(seq_num(dat))
        else:
            return check_complex(seq_num(dat))
