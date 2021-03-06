from chesspieces import Bishop, Knight, Pawn, Queen, Rook, WHITE, BLACK, opponent


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

    def make_board_piece(self, row, col, piecename, color):
        '''Создает фигуру piece и ставит ее в клетку row, col на доске'''
        self.field[row][col] = piecename(row, col, color)

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

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def set_up_default_arrangement(self):
        # расставляем фигуры:
        for i in range(8):  # пешки
            self.make_board_piece(1, i, Pawn, BLACK)
            self.make_board_piece(7, i, Pawn, WHITE)

        current_color = WHITE
        for i in range(0, 8, 7): # остальные
            # ладьи
            self.make_board_piece(i, 0, Rook, current_color)
            self.make_board_piece(i, 7, Rook, current_color)
            # кони
            self.make_board_piece(i, 1, Knight, current_color)
            self.make_board_piece(i, 6, Knight, current_color)
            # слоны
            self.make_board_piece(i, 2, Bishop, current_color)
            self.make_board_piece(i, 5, Board, current_color)
            # ферзь
            self.make_board_piece(i, 3, Queen, current_color)
            current_color = BLACK
