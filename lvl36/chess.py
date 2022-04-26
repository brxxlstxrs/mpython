WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


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


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def change_cell(self, row, col, piece):
        self.field[row][col] = piece

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def is_under_attack(self, row, col, color):
        '''Функция проверяет находится ли точка (row, col) под атакой хотя бы одной
        фигуры цвета color и возращает значение True/False, в зависимости от
        результата'''
        for i in self.field:
            for piece in i:
                if piece is not None and piece.get_color() == color:
                    if piece.can_move(row, col):
                        return True
        return False


    def way_is_clear(self, row, col, row1, col1):
        '''Проверяет свободен ли путь, возращает True/False'''
        dy = 0
        dx = 0
        if row1 > row:
            dy = 1
        elif row1 < row:
            dy = -1
        if col1 > col:
            dx = 1
        elif col1 < col:
            dx = -1
        row_now, col_now = row + dy, col + dx
        while row_now != row1 and col_now != col1:
            if self.field[row_now][col_now] is not None:
                return False
            row_now += dy
            col_now += dx
        if self.field[row_now][col_now] is not None:
            if self.field[row_now][col_now].get_color() == self.color:
                return False
        return True


    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False

        if type(piece) is not Knight:  # если фигура не является Конем
            if not self.way_is_clear(row, col, row1, col1):
                # если на пути есть мешающие фигуры
                return False

        self.change_cell(col, row, None)  # Снять фигуру.
        self.change_cell(col1, row1, piece)  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def set_up_default_arrangement(self):
        # расставляем фигуры:
        for i in range(8):  # пешки
            self.change_cell(1, i, Pawn)
            self.change_cell(7, i, Pawn)
        for i in range(0, 8, 7): # остальные
            # ладьи
            self.change_cell(i, 0, Rook)
            self.change_cell(i, 7, Rook)
            # кони
            self.change_cell(i, 1, Knight)
            self.change_cell(i, 6, Knight)
            # слоны
            self.change_cell(i, 2, Bishop)
            self.change_cell(i, 5, Board)
            # ферзь
            self.change_cell(i, 3, Queen)


def print_board(board): # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    board.set_up_default_arrangement()  # расставляем фигуры
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


if __name__ == '__main__':
    main()
