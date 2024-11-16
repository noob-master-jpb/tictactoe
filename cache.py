import csv
import log
import random

def clear():
    file = open('cache.csv', 'w',newline='')
    writer = csv.writer(file)
    writer.writerows([['h', 'c'], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ], ['7', ''], ['8', ''],
                     ['9', '']])

def cache_store(seq = []):
    if log.ret_cache_status():
        file = open('cache.csv', 'r+', newline='')
        reader = csv.DictReader(file)
        st = list(reader)
        file1 = open('cache.csv', 'w+', newline='')
        writer = csv.DictWriter(file1, ['h', 'c'])
        for i in st:
            if i['h'] == str(seq[0]):
                if str(seq[1]) not in i['c']:
                    i['c'] = i["c"] + str(seq[1])
        writer.writeheader()
        writer.writerows(st)
        file.flush()
        file.close()

def cache_move(seq = []):
    file = open('cache.csv', 'r+', newline='')
    reader = csv.DictReader(file)
    st = list(reader)
    temp = []
    for i in st:
        if i['h'] == str(seq[0]):
            for p in i['c']:
                temp.append(p)
    file.flush()
    file.close()
    return random.choice(temp)

