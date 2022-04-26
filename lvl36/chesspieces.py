from colors import WHITE, BLACK, opponent


class ChessPiece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
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


class Pawn(ChessPiece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.icon = 'P'
 
    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
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
        if self.row + direction == row:
            return True
 
        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True
 
        return False


class Rook(ChessPiece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.icon = 'R'

    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False
        return True


class Knight(ChessPiece):
    move = {2, 1}  # ход коня - два шага вперед и оин в сторону

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.icon = 'N'
 
    def can_move(self, row, col):
        # Предотвращение выхода за пределы доски
        if not self.on_board(row, col):
            return False

        # Проверка хода на валидность
        if set(map(abs, (self.row - row, self.col - col))) == Knight.move:
            return True
        return False


class Bishop(ChessPiece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.icon = 'B'
 
    def can_move(self, row, col):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        return False


class Queen(ChessPiece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.icon = 'Q'

    def can_move(self, row, col):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        if self.row != row and self.col != col:
            return False
        return True
