import log
import main
import cache

sts = 0
pros = ''

help = '# 1 = ON \n# 0 = OFF \n COMMAND LIST: \n /CACHE (0/1) \n /LOG (0/1) \n /PLAY CACHE (0/1) \n /STATUS(CACHE/PLAY CACHE/LOG) \n /RESET (STATUS/CACHE/ALL) '
def inp():
    global pros
    try:
        pros = str(input('---> '))
    except ValueError:
        pros = str(input('---> '))
        if log.ret_log_status() == 0:
            print('Invalid Input')
        else:
            print('Invalid command')
pros.lstrip(' ')
stts = 0
print('Type START to start game')
print('Quit to exit')
while stts == 0:
    inp()
    if pros.upper() == 'START':
        print('THE BOARD IS AS FOLLOWS \n'
              '[1 2 3]\n'
              '[4 5 6]\n'
              '[7 8 9]\n'
              'ENTER THE NUMBER SAME AS THE NUMBER GIVEN IN THE POSITION ABOVE\n')
        sts = 1
        stts = 1
    elif pros.upper() == 'QUIT':
        stts = 1
    elif pros.upper() == '/CACHE 1':
        log.cache_toggle(1)
    elif pros.upper() == '/CACHE 0':
        log.cache_toggle(0)
    elif pros.upper() == '/LOG 0':
        log.log_toggle(0)
    elif pros.upper() == '/LOG 1':
        log.log_toggle(1)
    elif pros.upper() == '/STATUS CACHE':
        log.ret_cache_status(1)
    elif pros.upper() == '/STATUS LOG':
        log.ret_log_status(1)
    elif pros.upper() == '/PLAY CACHE 0':
        log.play_cache_toggle(0)
    elif pros.upper() == '/PLAY CACHE 1':
        log.play_cache_toggle(1)
    elif pros.upper() == '/STATUS PLAY CACHE':
        log.ret_play_cache_status(1)
    elif pros.upper() == '/RESET STATUS':
        log.reset_default()
    elif pros.upper() == '/RESET CACHE':
        cache.clear()
    elif pros.upper() == '/RESET ALL':
        log.reset_default()
        cache.clear()
    elif pros.upper() == '/HELP':
        print(help)
    else:
        print('INVALID COMMAND')
cts = 1
while sts == 1:
    if cts == 1:
        main.start()
    print('Do you want to play again? y/n')
    try:
        s = input('--->')
        if s.upper() == 'N':
            sts = 0
        elif s.upper() == 'Y':
            cts = 1
        else:
            cts = 0
            print("Invalid Input")
    except ValueError:
        print("Invalid Input")
        s = input('--->')
