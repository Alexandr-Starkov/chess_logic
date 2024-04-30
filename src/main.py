
class Board:
    def __init__(self, width=8, heigth=8):
        self.width = width
        self.height = heigth
        self.board = []

    def create_board(self):
        '''Board creation'''
        for i in range(self.height):
            if i < 2:
                self.board.append(['x'] * self.width)
            elif i in (self.width - 2, self.width - 1):
                self.board.append(['x'] * self.width)
            else:
                self.board.append([' '] * self.width)

    def draw_board(self):
        print('-' * (self.width * 4 + 1))

        for i in range(len(self.board)):
            row = '| ' + ' | '.join(self.board[i]) + ' |'
            print(row)

        print('-' * (self.width * 4 + 1))

