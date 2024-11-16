import tree_function as tf

tree_handler = tf.tree(9)

database_handler = open('tree_database.txt','r')

database = database_handler.readlines()[0]

temp = []

def index_data(lis=[]):
    if not lis:
        return
    temp = []
    for i in lis:
        temp.append(int(database[int(i)]))
    return temp

def data_index(lis=[]):
    if not lis:
        return
    temp = []
    initindex = index_data(tree_handler.level_range(1)).index(lis[0])
    temp.append(initindex)
    for i in range(len(lis) - 1):
        tindex = index_data(tree_handler.ret_child(initindex)).index(lis[i + 1])
        trdex = tree_handler.ret_child(initindex)[tindex]
        initindex = trdex
        temp.append(initindex)
    return temp


def traceback_index(list=[]):
    initindex = index_data(tree_handler.level_range(1)).index(list[0])
    for i in range(len(list) - 1):
        tindex = index_data(tree_handler.ret_child(initindex)).index(list[i + 1])
        trdex = tree_handler.ret_child(initindex)[tindex]
        initindex = trdex
    return initindex


def branchout(lis=[]):
    if not lis:
        return
    lisindex = data_index(lis)
    index = traceback_index(lis)
    temp = []
    result = []
    for i in tree_handler.ret_child(index):
        temp.append(lisindex+[i])
    if len(temp) == 1:
        # print(temp[0])
        return temp[0]
    # print(temp)
    for i in temp:
        result += branchout(index_data(i))
    return result

def branchout2(lis=[]):
    if not lis:
        return []

    # Initialize a stack to store nodes to be processed
    stack = [lis]
    result = []

    while stack:
        # Pop a node from the stack
        current_node = stack.pop()

        # Get the index of the current node
        lisindex = data_index(current_node)
        print("lisindex:", lisindex)
        index = traceback_index(current_node)
        print("index:", index)

        # Get the children of the current node
        children = tree_handler.ret_child(index)

        # If there's only one child, add its index to the result
        if len(children) == 1:
            result.append(lisindex + [children[0]])
        else:
            # If there are multiple children, add the indices of all its children to the stack
            for child in children:
                stack.append(lisindex + [child])

    return result



def refinelist(fin):
    temp = []
    for i in range(0,len(fin),9):
        temp.append(index_data(fin[i:i+9]))
    return temp


def trigger_branching(lis):
    return refinelist(branchout(lis))

