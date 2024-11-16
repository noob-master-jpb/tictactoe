import data

class node:

    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
        self.win = None
        # par = self.parent
        # if self.parent = '0':
        #     self.seq= []

    def add(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix, self.data)
        if self.child:
            for child in self.child:
                child.print_tree()


root = node('0')
n1 = node('1')
n2 = node('2')
n3 = node('3')
n4 = node('4')
n5 = node('5')
n6 = node('6')
n7 = node('7')
n8 = node('8')
n9 = node('9')

li = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

for i in li:
    root.add(i)
    for j in li:
        if j != i:
            i.add(node(j.data))

def ins_node(root):
    if root:
        for h in root.child:
            if h:
                for y in root.child:
                    if y!= h :
                        h.add(node(y.data))

for o1 in root.child:
    ins_node(o1)
    for o2 in o1.child:
        ins_node(o2)
        for o3 in o2.child:
            ins_node(o3)
            for o4 in o3.child:
                ins_node(o4)
                for o5 in o4.child:
                    ins_node(o5)
                    for o6 in o5.child:
                        ins_node(o6)
                        for o7 in o6.child:
                            ins_node(o7)

file = open('../not in use/storen.txt', 'a+')

def database_print(root,m=0):
    m+=1
    for t in root.child:
        print('  '*m,'|_',t.data)
        # gola = str('  '*m+'|_'+t.data,'\n')
        # file.writelines('  '*m+'|_'+t.data+'\n')
        database_print(t,m)


def goll(dat,m=0,temp = None):
    if not temp:
        temp = [0,0,0,0,0,0,0,0,0]
    if dat.child != []:
        m += 1
        for i in dat.child:
            # print(f"m = {m} i ={i.data}")
            temp[m-1] = i.data
            goll(i,m,temp)
    else:
        if data.win_check(temp):
            dat.win = 1
        else:
            dat.win = 0

def inline(root):
    for i in root.child:
        print(i.data, i.get_level())

filest = open("../extraction/rawdata.txt", 'w+')
def getti(root,m=0):
    m+=1
    for t in root.child:
        print(t.get_level(),t.data)
        filest.write(str(t.get_level())+' '+str(t.data)+'\n')
        filest.flush()
        getti(t,m)

getti(root)
filest.close()

