import log
import main_set as ms
import data
import Translator as trs
import random
import calculator as rcal
import cache

def start():
    play = ms.tic()

    def show_board_playable():
        play.display(trs.num_board(play.prep_board()))

    def c_play(play):
        play.take_input(rcal.start_counting(play.seq, play.mode))
        play.update_board_whole(trs.seq_num(play.seq))
        show_board_playable()

    def v_play(play):
        play.take_input(int(cache.cache_move(play.seq)))
        play.update_board_whole(trs.seq_num(play.seq))
        show_board_playable()


    def h_play(play):
        play.take_input(play.make())
        show_board_playable()
        print('---------------')

    print("choose dificulty")
    print('Easy = 1')
    print('Hard = 2')
    print('Very Hard = 3')
    ctrl = 0

    while not ctrl:
        try:
            diff = int(input("Enter Difficulty = "))
            ctrl = 1
        except ValueError:
            print("not allowed")

    diff = str(diff)
    prob = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if random.choice(prob) > 10 - (int(diff)) ** int(diff):
        play.mode = 2
    else:
        play.mode = 1
    # 1 = human and 2 = computer start

    play.status = 1

    verdict = False
    if play.mode == 1:
        print("You Start (X)")
        show_board_playable()
        while play.ret_status_full():
            if len(play.seq) == 2:
                if log.ret_cache_status() == 1:
                    cache.cache_store(play.seq)
            if log.ret_log_status():
                print(play.board)
            if play.status == 1:
                h_play(play)
                play.status = 2
                if data.check_complex(trs.alternate_board(play.board)) == 0:
                    print("YOU WIN :)")
                    verdict = True
                    break
            elif play.status == 2:
                if len(play.seq) == 1:
                    if log.ret_play_cache_status() == 1:
                        v_play(play)
                    else:
                        c_play(play)
                else:
                    c_play(play)
                play.status = 1
                if data.check_complex(trs.alternate_board(play.board)) == 1:
                    print("COMPUTER WINS :D")
                    verdict = True
                    break

        if (not play.ret_status_full()) and (verdict == False):
            h_play(play)
            if data.check_complex(trs.alternate_board(play.board)) == 0:
                print("YOU WIN :)")
            elif data.check_complex(trs.alternate_board(play.board)) == -1:
                print("ITS A TIE -_-")
            elif data.check_complex(trs.alternate_board(play.board)) == 1:
                print('COMPUTER WINS :D')
            else:
                print('program finished with errors')

    elif play.mode == 2:
        print("Computer Starts (X)")
        play.take_input(rcal.difficulty(int(diff)))
        play.update_board_whole(trs.seq_num(play.seq))
        show_board_playable()
        if log.ret_log_status():
            print(play.board)
        while play.ret_status_full():
            if play.status == 1:
                h_play(play)
                play.status = 2
                if data.check_complex(play.board) == 0:
                    print("YOU WIN :)")
                    verdict = True
                    break
            elif play.status == 2:
                try:
                    c_play(play)
                    play.status = 1
                    if data.check_complex(play.board) == 1:
                        print("COMPUTER WINS :D")
                        verdict = True
                        break
                except TypeError:
                    print("The game has ended due to an error")
                    verdict = True
                    break
        if (not play.ret_status_full()) and (verdict == False):
            play.take_input(play.board.index(0) + 1)
            play.update_board_whole(trs.seq_num(play.seq))
            show_board_playable()
            print("ITS A TIE -_-")

