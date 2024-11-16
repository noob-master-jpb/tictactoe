import math

uniq = 9
file = open('online.txt','r')
tree = file.read()



def singlelevel(depth,uni):
    fac = math.factorial(uni)/math.factorial(uni-depth)
    return int(fac)

def uptolevel(dep,it):
    store = 0
    for i in range(1,dep+1):
        store+= singlelevel(i,it)
    return store

def retdepth(index,it):
    if index < 0:
        return 0
    maxdepth = uptolevel(it,it)
    for i in range(1,it+1):
        if uptolevel(i,it)>index:
            return i
        elif index> maxdepth:
            print("out of range")
            return

def levelrange(depth,it):
    max = int(uptolevel(depth,it))
    min = int(uptolevel(depth-1,it)+1)
    return range(min,max+1)

def childdepth(index,it):
    depth = retdepth(index, it)
    if depth < it:
        return depth+1
    else:
        print('item does not have any child')
        return None

def parentdepth(index,it):
    depth = retdepth(index,it)
    if depth:
        if depth <= it:
            return depth-1
    else:
        print('Parent is Source')
        return

def retchild(index,it):
    depth = retdepth(index,it)
    child_depth = childdepth(index,it)
    if not child_depth:
        return
    parentdata = singlelevel(depth,it)
    childdata = singlelevel(child_depth,it)
    ratio = int(childdata/parentdata)
    starting_index = parentdata+(ratio*index)+1
    childlist = []
    for i in range(starting_index,starting_index+ratio):
        childlist.append(i)
    return childlist

def retparent(index,it):
    depth = retdepth(index,it)
    pardepth = parentdepth(index,it)
    if not pardepth:
        return
    cseg = int((index-6)/4)
    parentdata = singlelevel(pardepth,it)
    parent = range(parentdata)[cseg]
    return parent

print(retparent(6,5))