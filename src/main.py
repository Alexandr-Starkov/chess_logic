from typing import List


class Figure:
    def __init__(self) -> None:
        self.identity = 'n'

    def move(self):
        pass

    def cut_an_enemy_figure(self):
        pass


class Pawn(Figure):
    def __init__(self):
        self.identity = 'p'

    @staticmethod
    def create_pawns():
        pawns = []

        for i in range(1, 17):
            p = Pawn()
            p.id = i
            pawns.append(p)

        return pawns


class Knight(Figure):
    @staticmethod
    def create_knights(self):
        pass


class Bishops(Figure):
    @staticmethod
    def create_bishops(self):
        pass


class Rook(Figure):
    @staticmethod
    def create_rooks(self):
        pass


class Queen(Figure):
    @staticmethod
    def create_queen(self):
        pass


class King(Figure):
    @staticmethod
    def create_king():
        pass


class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = []

    def create_board(self):
        '''Board creation'''
        for i in range(self.height):
            # figures of the first two lines
            if i < 2:
                self.board.append([' '] * self.width)
            # figures of the last two lines
            elif i in (self.width - 2, self.width - 1):
                self.board.append([' '] * self.width)
            else:
                self.board.append([' '] * self.width)

    def draw_board(self):
        '''board drawing'''
        # line before board
        line = '  ' + '-' * (self.width * 4 + 1)
        print(line)

        # draw board with figures
        for row, char in zip(range(len(self.board)), ('ABCDEFGH')):
            row_items = []
            for item in self.board[row]:
                if isinstance(item, Figure):
                    row_items.append(item.identity)
                else:
                    row_items.append(' ')
            row = char + ' | ' + ' | '.join(row_items) + ' |'
            print(row)

        # line after board
        line = '  ' + '-' * (self.width * 4 + 1)
        print(line)

        # digits after board
        digits = '    1   2   3   4   5   6   7   8'
        print(digits)

    def insert_figure(self, figure_list: List[Figure]):
        '''add player figures to the field'''
        for index, figure in enumerate(figure_list):
            if figure.identity == 'p':  # pawns
                if index <= 7:
                    self.board[1][index] = figure
                else:
                    self.board[6][index - 8] = figure

    def prepare_figure(self):
        '''figure preparation'''
        p = Pawn()
        figures = []

        pawns_list = p.create_pawns()
        figures.extend(pawns_list)

        self.insert_figure(figures)

    def shape_labels(self):
        '''description of all the designations in the game'''
        info = '''
Legend
p - pawn(пешка)
k - knight(конь)
b - bishop(слон)
r - rook(ладья)
q - queen(ферзь)
k - king(король)
'''
        print(info)
