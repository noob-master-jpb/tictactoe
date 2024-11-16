# not working-----------------------------------------

b = [[0 for i in range(3)] for j in range(3)]
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]


def show(list):
    for i in list:
        print(i)


def make(list):
    n = int(input('---'))
    m = str(n)
    row = int(m[0])-1
    col = int(m[1])-1

    if (row <= 3) and (col <= 3):
        list[row][col] = 1
        show(list)
        print('')
    else:
        print('invalid')


def switch(back):
    back[0], back[2] = back[2], back[0]


def convert_HV(list):
    back = list
    new = []
    for c in range(0, 3):
        tem = []
        for i in back:
            tem.append(i[c])
        new.append(tem)
    return new


def convert_D(list):
    back = list
    new = []
    c = 0
    for i in back:
        new.append(i[c])
        c += 1
    return new


def convert_D_Rev(list, data):
    back = list
    for i in data:
        ind = data.index(i)
        back[ind][ind] = i
    return back


def xconvert_D(list):
    back = list
    new = []
    switch(back)
    c = 0
    for i in back:
        new.append(i[c])
        c += 1
    switch(back)
    switch(new)
    return new


def xconvert_D_Rev(list, data):
    back = list
    switch(back); switch(data)
    for i in data:
        ind = data.index(i)
        back[ind][ind] = i
    switch(back)
    return back


def data_control.check(item):
    use = item
    c = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    if use in c:
        ind = use.index(0)
        use[ind] = 2
    return use


def h_check(list):
    back = list
    for id in back:
        ink = back.index(id)
        out = data_control.check(id)
    back[ink] = out
    return back


def v_check(list):
    back = list; back = convert_HV(back)
    for id in back:
        ink = back.index(id); out = data_control.check(id)
    back[ink] = out
    back = convert_HV(back)
    return back

def ad_check(list):
    back = list
    tempdata = convert_D(back)
    data = data_control.check(tempdata)
    convert_D_Rev(back,data)
    return back
def xd_check(list):
    back = list
    tempdata = xconvert_D(back)
    data = check(tempdata)
    xconvert_D_Rev(back, data)
    return back

def d_check(list):
    back = list
    ad_check(back)
    if back == list:
        xd_check(back)
    return back


def defend(list):
    back = list
    while True:
        vir = h_check(back)
        show(vir)
        break
    return back

while True:
    make(b)
    b = h_check(b)
    show(b)
