import data
import Translator as trs


class tic:

    def __init__(self):
        self.board = [0] * 9
        self.seq = []
        self.mode = 0
        self.status = 0
    def prep_board(self):  # convert the list into a matrix
        data = self.board
        data = [data[j:j + 3] for j in range(0, 9, 3)]
        return data

    def display(self, seq):
        for i in seq:
            print(i)

    def ret_status_full(self):
        if self.board.count(0) > 1:
            return True
        else:
            return False

    def take_input(self, inp):
        if not len(self.seq) > 9:
            self.seq.append(inp)

    def make(self):  # takes input from the user and updates the board
        # data = self.prep_board()
        # self.board = data.make(self.board,self.mode)
        ct = 0
        while not ct:
            try:
                n = int(input('----'))
                ct = 1
                if (n <= 9) and (n >= 1):
                    self.board[n - 1] = self.mode
                    return n
                else:
                    ct = 0
                    print('Enter number between 1 - 9')
            except ValueError:
                print('Enter number between 1 - 9')



    def prep_display_board(self):  # displays the list in three parts without being a matrix
        data.show(self.board)

    def raw_show(self):  # prints the list
        print(self.board)

    def defend(self):  # defends the board
        self.board = data.defend(self.board)

    def update_board_whole(self, lis):
        self.board = list(lis)

    def update_board(self, item, index):
        self.board[index] = item


class index:
    def __init__(self):
        self.row = [i for i in range(0, 9)]
        self.col = [i + j for j in range(0, 3) for i in range(0, 9, 3)]
        self.dig = [i for i in range(0, 9, 4)]
        self.rdig = [i for i in range(2, 8, 2)]
        self.mid = [i for i in range(1, 8, 2)]
        self.corner = [i for i in range(0, 10, 2) if i != 4]
        self.center = [4]

    def prep(self, data):
        data = [data[j:j + 3] for j in range(0, 9, 3)]
        return data

    def prep_row(self):
        data = [self.row[j:j + 3] for j in range(0, 9, 3)]
        return data

    def prep_col(self):
        data = [self.col[j:j + 3] for j in range(0, 9, 3)]
        return data


class value:
    def __init__(self, board):
        ind = index()
        ti = tic()

        self.rows_value = data.h_data(board)
        self.row1_value = self.rows_value[0]
        self.row2_value = self.rows_value[1]
        self.row3_value = self.rows_value[2]

        self.cols_value = data.v_data(board)
        self.col1_value = self.cols_value[0]
        self.col1_value = self.cols_value[1]
        self.col2_value = self.cols_value[2]

        self.dig_value = data.d_data(board)
        self.rdig_value = data.rd_data(board)

        self.mid_value = []
        for mi in board:
            ink = board.index(mi)
            if ink in ind.mid:
                self.mid_value.append(mi)

        self.corner_value = []
        for cr in board:
            if cr in ind.corner:
                self.corner_value.append(cr)

        self.center_value = board[4]


a = tic()
a_value = value(a.board)
