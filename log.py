import csv


def reset_default():
    file = open('log_status.csv', 'w+', newline='')
    writer = csv.writer(file)
    writer.writerows([['name', 'status'], ['cache', '0'], ['log', '0'], ['play_cache', '0']])
    file.flush()
    file.close()


def ret_cache_status(z=0):
    file = open('log_status.csv', 'r', newline='')
    reader = csv.DictReader(file)
    for i in reader:
        if i['name'] == 'cache':
            if i['status'] == '1':
                file.close()
                if z == 1:
                    print('Cache = On')
                return 1
            elif i['status'] == '0':
                file.close()
                if z == 1:
                    print('Cache = Off')
                return 0
            else:
                print('corrupted log status')
                file.close()
                return



def ret_log_status(z=0):
    file = open('log_status.csv', 'r', newline='')
    reader = csv.DictReader(file)
    for i in reader:
        if i['name'] == 'log':
            if i['status'] == '1':
                file.close()
                if z == 1:
                    print('log = On')
                return 1
            elif i["status"] == '0':
                file.close()
                if z == 1:
                    print('log = Off')
                return 0
            else:
                file.close()
                print('Corrupted log status')
                return



def ret_play_cache_status(z=0):
    file = open('log_status.csv', 'r', newline='')
    reader = csv.DictReader(file)
    for i in reader:
        if i['name'] == 'play_cache':
            if i['status'] == '1':
                file.close()
                if z == 1:
                    print('play_cache is On')
                return 1
            elif i["status"] == '0':
                file.close()
                if z == 1:
                    print('play_cache is Off')
                return 0
            else:
                file.close()
                print('Corrupted log status')
                return



def cache_toggle(a=0):
    z = 0
    file = open('log_status.csv', 'r+', newline='')
    reader = csv.DictReader(file)
    st = list(reader)
    file1 = open('log_status.csv', 'w+', newline='')
    writer = csv.DictWriter(file1, ['name', 'status'])
    for i in st:
        if i['name'] == 'cache':
            i['status'] = a
            if a == 0:
                print('Cache = Off')
            elif a == 1:
                print('Cache = On')
    writer.writeheader()
    writer.writerows(st)


def log_toggle(a=0):
    z = 0
    file = open('log_status.csv', 'r+', newline='')
    reader = csv.DictReader(file)
    st = list(reader)
    file1 = open('log_status.csv', 'w+', newline='')
    writer = csv.DictWriter(file1, ['name', 'status'])
    for i in st:
        if i['name'] == 'log':
            i['status'] = a
            if a == 0:
                print('log = Off')
            elif a == 1:
                print('log = On')
    writer.writeheader()
    writer.writerows(st)


def play_cache_toggle(a=0):
    z = 0
    file = open('log_status.csv', 'r+', newline='')
    reader = csv.DictReader(file)
    st = list(reader)
    file1 = open('log_status.csv', 'w+', newline='')
    writer = csv.DictWriter(file1, ['name', 'status'])
    for i in st:
        if i['name'] == 'play_cache':
            i['status'] = a
            if a == 0:
                print('play_cache = Off')
            elif a == 1:
                print('play_cache = On')
    writer.writeheader()
    writer.writerows(st)


# def ret_play_cache_status(z=0):
#     file = open('log_status.csv', 'r', newline='')
#     reader = csv.DictReader(file)
#     for i in reader:
#         if i['name'] == 'log':
#             if i['status'] == '1':
#                 file.close()
#                 if z == 1:
#                     print('play_cache is On')
#                 return 1
#             elif i["status"] == '0':
#                 file.close()
#                 if z == 1:
#                     print('play_cache is Off')
#                 return 0
#             else:
#                 file.close()
#                 print('Corrupted log status')
#                 return
#         else:
#             print('play_cache status not found')
