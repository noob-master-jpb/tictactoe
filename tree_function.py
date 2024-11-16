import math

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
    range_max = int(uptolevel(depth,it))
    range_min = int(uptolevel(depth-1,it))
    return range(range_min,range_max)

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
    child_start = ((index-int(levelrange(depth,it)[0]))*(it-depth))+(int(levelrange(depth,it)[0])+singlelevel(depth,it))
    children = [i for i in range(child_start,child_start+(it-depth))]
    return children


def retparent(index,it):
    depth = retdepth(index,it)
    pardepth = parentdepth(index,it)
    if not pardepth:
        return
    cseg = int((index-6)/4)
    parentdata = singlelevel(pardepth,it)
    parent = range(parentdata)[cseg]
    return parent

class tree:

    def __init__(self,item):
        self.item = item

    def assign(self,item):
        self.item = item

    def data_level(self,death):
        return singlelevel(death,self.item)

    def data_upto_level(self,depth):
        return singlelevel(depth,self.item)

    def re_depth(self,index):
        return retdepth(index,self.item)

    def level_range(self,depth):
        return levelrange(depth,self.item)

    def child_depth(self,index):
        return childdepth(index,self.item)

    def parent_depth(self,index):
        return parentdepth(index,self.item)

    def ret_child(self,index,):
        return retchild(index,self.item,)

    def ret_parent(self,index):
        return retparent(index,self.item)



