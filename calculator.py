import Handler as han
import data
import random
import log

def int_type(dic={}):
    for i in dic.values():
        if i > 0:
            return True
    return False


def ret_max(dic={}):
    uid = []
    reval = []
    for i in list(dic.values()):
        if i != 0:
            reval.append(i)
    if not reval:
        if log.ret_cache_status() == 1:
            print('#error : probably the game has ended')
        return
    c = max(reval)
    if not c:
        return 0
    for i in dic.keys():
        if dic[i] == c:
            uid.append(i)
    return uid


def tie_cal(tie, avg):
    if ret_max(tie):
        if len(ret_max(tie)) > 1:
            temp = {}
            ftemp = []
            for h in ret_max(tie):
                temp[h] = avg[h]
            c = max(temp.values())
            for g in temp.keys():
                if temp[g] == c:
                    ftemp.append(g)

            return random.choice(ftemp)
        else:
            return random.choice(ret_max(tie))
    else:
        return


def start_counting(seq, mode=0):
    win = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}  # stores the no of wins
    lose = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    tie = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    avg = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    if log.ret_log_status() == 1:
        print('branching')
    else:
        print('Wait....')
    st = han.trigger_branching(seq)
    if log.ret_log_status() == 1:
        print('calculating')# will provide the rest of the sequence from a point
    else:
        print('loading')
    for i in st:
        result = data.step_check_complex(i)
        w_val = i[len(seq)]
        if result == 0:
            lose[w_val] += 1
        elif result == 1:
            win[w_val] += 1
        elif result == -1:
            tie[w_val] += 1
        else:
            if result != 2:
                print('Invalid result')

    if mode == 2:
        for f in avg.keys():
            avg[f] = win[f] - lose[f]
    elif mode == 1:
        for f in avg.keys():
            avg[f] = lose[f] - win[f]
    if log.ret_log_status() == 1:
        print('win  ', win)
        print('lose ', lose)
        print('tie  ', tie)
        print('avg  ', avg)
        print(data.show(data.seq_num(seq)))

    if mode == 1:
        if int_type(avg):
            if ret_max(avg):
                return random.choice(ret_max(avg))
            else:
                return tie_cal(tie, avg)
        else:
            if len(seq) > 1:
                return tie_cal(tie, avg)
            else:
                return random.choice(ret_max(avg))
    elif mode == 2:
        if int_type(avg):
            if ret_max(avg):
                return random.choice(ret_max(avg))
            else:
                return tie_cal(tie, avg)
        else:
            return random.choice(ret_max(avg))


def difficulty(level):
    if level == 1:
        return random.choice([2, 4, 6, 8])
    elif level == 2:
        return random.choice([1, 3, 5, 7, 9])
    elif level == 3:
        return 5
    elif level > 3:
        print("***INVALID INPUT*** Selecting The Highest Difficulty")
        return 5
    else:
        print('***INVALID INPUT*** Selecting the Lowest Difficulty')
        return random.choice([2, 4, 6, 8])

# sep = [1]  # test seq
# for i in range(1,10):
#     print(start_counting([i], 1))

# if 2 tie has the same value it should check for the avg of same indexes and decide which one has the higher avg
