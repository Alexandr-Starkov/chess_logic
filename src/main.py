from colorama import Fore
from typing import List


class Figure:
    def __init__(self) -> None:
        self.identity = 'n'

    def move(self):
        pass

    def cut_an_enemy_figure(self):
        pass


class Pawn(Figure):
    def __init__(self, color):
        self.identity = '♟︎'
        self.color = color

    @staticmethod
    def create_pawns():
        pawns = []
        for i in range(0, 16):
            if i <= 7:
                p = Pawn(Fore.BLACK)
                p.id = i
                p.user = 'player-2'
                pawns.append(p)
            else:
                i -= 8
                p = Pawn(Fore.RED)
                p.id = i
                p.user = 'player-1'
                pawns.append(p)

        return pawns


class Knight(Figure):
    def __init__(self, color) -> None:
        self.identity = '♞'
        self.color = color

    @staticmethod
    def create_knights():
        knights = []
        for i in range(0, 4):
            if i < 2:
                k = Knight(Fore.BLACK)
                k.id = i
                k.user = 'player-2'
                knights.append(k)
            else:
                i -= 2
                k = Knight(Fore.RED)
                k.id = i
                k.user = 'player-1'
                knights.append(k)

        return knights


class Bishop(Figure):
    def __init__(self, color) -> None:
        self.identity = '♝'
        self.color = color

    @staticmethod
    def create_bishops():
        bishops = []
        for i in range(0, 4):
            if i < 2:
                b = Bishop(Fore.BLACK)
                b.id = i
                b.user = 'player-2'
                bishops.append(b)
            else:
                i -= 2
                b = Bishop(Fore.RED)
                b.id = i
                b.user = 'player-1'
                bishops.append(b)

        return bishops


class Rook(Figure):
    def __init__(self, color) -> None:
        self.identity = '♜'
        self.color = color

    @staticmethod
    def create_rooks():
        rooks = []
        for i in range(0, 4):
            if i < 2:
                r = Rook(Fore.BLACK)
                r.id = i
                r.user = 'player-2'
                rooks.append(r)
            else:
                i -= 2
                r = Rook(Fore.RED)
                r.id = i
                r.user = 'player-1'
                rooks.append(r)

        return rooks


class Queen(Figure):
    def __init__(self, color) -> None:
        self.identity = '♛'
        self.color = color

    @staticmethod
    def create_queen():
        queens = []
        for i in range(0, 2):
            if i < 1:
                q = Queen(Fore.BLACK)
                q.id = i
                q.user = 'player-2'
                queens.append(q)
            else:
                i -= 1
                q = Queen(Fore.RED)
                q.id = i
                q.user = 'player-1'
                queens.append(q)

        return queens


class King(Figure):
    def __init__(self, color) -> None:
        self.identity = '♚'
        self.color = color

    @staticmethod
    def create_king():
        kings = []
        for i in range(0, 2):
            if i < 1:
                k = King(Fore.BLACK)
                k.id = i
                k.user = 'player-2'
                kings.append(k)
            else:
                i -= 1
                k = King(Fore.RED)
                k.id = i
                k.user = 'player-1'
                kings.append(k)

        return kings


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
                    if row < 2:
                        row_items.append(
                            item.color + item.identity + Fore.RESET)
                    elif row >= 6:
                        row_items.append(
                            item.color + item.identity + Fore.RESET)
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
        '''add player figures to the field
        field [0], field[1] - player-2 side
        field [6], field[7] - player-1 side
        '''
        for index, figure in enumerate(figure_list):
            if figure.identity == '♟︎':  # pawns
                if index <= 7:
                    self.board[1][index] = figure
                else:
                    self.board[6][index - 8] = figure
            elif figure.identity == '♞':  # knights
                if index == 16:
                    self.board[0][1] = figure
                elif index == 17:
                    self.board[0][6] = figure
                elif index == 18:
                    self.board[7][1] = figure
                elif index == 19:
                    self.board[7][6] = figure
            elif figure.identity == '♝':  # bishops
                if index == 20:
                    self.board[0][2] = figure
                elif index == 21:
                    self.board[0][5] = figure
                if index == 22:
                    self.board[7][2] = figure
                elif index == 23:
                    self.board[7][5] = figure
            elif figure.identity == '♜':  # rooks
                if index == 24:
                    self.board[0][0] = figure
                elif index == 25:
                    self.board[0][7] = figure
                if index == 26:
                    self.board[7][0] = figure
                elif index == 27:
                    self.board[7][7] = figure
            elif figure.identity == '♛':  # queen
                if index == 28:
                    self.board[0][4] = figure
                elif index == 29:
                    self.board[7][4] = figure
            elif figure.identity == '♚':  # king
                if index == 30:
                    self.board[0][3] = figure
                elif index == 31:
                    self.board[7][3] = figure

    def prepare_figure(self):
        '''figure preparation'''
        figures = []

        pawns_list = Pawn.create_pawns()
        knight_list = Knight.create_knights()
        bishop_list = Bishop.create_bishops()
        rook_list = Rook.create_rooks()
        queen_list = Queen.create_queen()
        king_list = King.create_king()

        for elements in (pawns_list, knight_list, bishop_list,
                         rook_list, queen_list, king_list):
            figures.extend(elements)

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


def main():
    board = Board()
    board.create_board()
    board.prepare_figure()
    board.draw_board()


if __name__ == '__main__':
    main()
