for i in st:
    result = data.step_check_complex(i)
    if result == 0:
        print(result,'Lose')
        print(data.show(data.seq_num(i)))
        print(data.seq_num(i))
        print(i)
    elif result == 1:
        print(result,"win")
        print(data.show(data.seq_num(i)))
        print(data.seq_num(i))
        print(i)
    elif result == 2:
        print(result,'Both')
        print(data.show(data.seq_num(i)))
        print(data.seq_num(i))
        print(i)
    elif result == -1:
        print(result,'Tie')
        print(data.show(data.seq_num(i)))
        print(data.seq_num(i))
        print(i)


import data
import Handler as han
sep = [5, 3, 9, 8, 7, 6, 4, 2, 1]

def step_check_conplex(seq):
    for i in range(5, len(seq)+1):
        dat = seq[:i]
        if data.check_complex(data.seq_num(dat)) == -1:
            if i == 9:
                return data.check_complex(data.seq_num(dat))
        else:
            return data.check_complex(data.seq_num(dat))

print(step_check_conplex(sep))