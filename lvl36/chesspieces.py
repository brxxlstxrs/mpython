from colors import WHITE, BLACK, opponent


class Pawn:
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'P'
 
    def get_color(self):
        return self.color
 
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


class Rook:
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'R'
 
    def get_color(self):
        return self.color
 
    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False
 
        return True


class Knight:
    move = {1, 2}

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'N'
 
    def get_color(self):
        return self.color

    @staticmethod
    def on_board(row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        return False

    def can_move(self, row, col):
        # Предотвращение выхода за пределы доски
        if not self.on_board(row, col):
            return False

        # Проверка хода на валидность
        if set(map(abs, (self.row - row, self.col - col))) == Knight.move:
            return True
        return False


class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'B'
 
    def get_color(self):
        return self.color

    @staticmethod
    def on_board(row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        return False

    def can_move(self, row, col):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        return False


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1
 
    def char(self):
        return 'Q'
 
    def get_color(self):
        return self.color

    @staticmethod
    def on_board(row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        return False

    def can_move(self, row, col):
        if not self.on_board(row, col):
            return False

        if abs(row - self.row) == abs(col - self.col):
            return True
        if self.row != row and self.col != col:
            return False
        return True
