file = open('rawdata.txt','r+')
refine = open('online.txt','w+')

alllist = file.readlines()
# print(alllist)

final = []

def com(ls=[]):
    c = ''
    for i in ls:
        c = c + str(i)
    return c
def ref(se):
    out = se[:-1]
    depth = int(out[0])
    data = int(out[-1])
    return depth,data

for i in range(1,10):
    temp = []
    for item in alllist:
        da = ref(item)
        if da[0] == i:
            temp.append(da[-1])
    refine.write(str(com(temp)))
    final.append(com(temp))


for i in final:
    print(i)