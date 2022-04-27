from colors import *


class ChessPiece:
    def __init__(self, color):
        self.color = color
        self.icon = 'd'  # дефолтный символ фигуры

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def char(self):
        return self.icon

    def get_color(self):
        return self.color

    @staticmethod
    def on_board(row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        return False
    
    def can_move(self, board, row, col, row1, col1):
        pass

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = 'P'
        
    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False
 
        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
 
        # ход на 1 клетку
        if row + direction == row1:
            return True
 
        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку,
        # которая не лежит в том же ряду или столбце клеток.
        if self.row != row and self.col != col:
            return False
        
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True


class Knight(ChessPiece):
    move = {2, 1}  # ход коня - два шага вперед и оин в сторону

    def __init__(self, color):
        super().__init__(color)
        self.icon = 'N'

    def can_move(self, board, row, col, row1, col1):
        # Предотвращение выхода за пределы доски
        if not self.on_board(row, col):
            return False

        # Проверка хода на валидность
        if set(map(abs, (self.row - row, self.col - col))) == Knight.move:
            return True
        return False


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = 'B'

    def can_move(self, board, row, col, row1, col1):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        return False


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = 'Q'

    def can_move(self, board, row, col, row1, col1):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        if self.row != row and self.col != col:
            return False
        return True
