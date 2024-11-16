import data


class board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.start_player = None
        self.turn = None
        self.seq = []

    def board_input(self, cords):
        self.board[cords] = 2
        self.seq.append(cords)

    def board_output(self):
        for i in range(0, 9, 3):
            print(self.board[i:i + 3])

    def board_out_defend(self):
        return data.defend(self.board)

    def board_update(self, lis):
        self.board = lis

    def check_win(self):
        return data.win_check(self.board)

    def board_raw(self):
        return self.board

    def board_seq_update(self,item):
        self.seq.append(item)


class cache:
    def __init__(self):
        self.turn = None
        self.current_pos = None
        self.seq = []
        self.state = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}