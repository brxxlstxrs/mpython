from colors import WHITE, BLACK, opponent
from chesspieces import Bishop, Knight, Queen, Rook


def define_the_direction_and_lenght(row, col, row1, col1):
    '''Определяет направление хода и его длину и возвращает их'''
    direction = ''
    if row1 > row:
        direction = 'top'
    else:
        direction = 'down'
    if col1 > col:
        direction += 'right'
    else:
        direction += 'left'

    if len(direction) < 6:  # если направление не диагонално
        if row1 == row:  # ход лево/прав длина соответствует abs(col1 - col)
            length = abs(col1 - col)  # длина
        else:  # ход вверх/вниз
            length = abs(row1 - row)  # длина
    else:  # если направление диагонально, то abs(row1 - row) == abd(col1 - col)
        lenght = abs(col1 - col)
    return direction, lenght  # type: ignore


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


    def get_line(self, x, y, d, length): # d -- направление
        '''Возвращает линию на доске от x, y длинной lenght, 
        с направлением direction'''
        dy = -1 if 'top' in d else 1 if 'down' in d else 0
        dx = -1 if 'left' in d else 1 if 'right' in d else 0
        return [self.field[y + dy * i][x + dx * i] for i in range(length)]

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
        if self.is_under_attack(row1, col1, piece.get_color()):
            return False
        if not piece.can_move(row1, col1):
            return False

        # определяем направление и длину хода
        direction, lenght = define_the_direction_and_lenght(row, col, row1, col1)

        move_line = self.get_line(row, col, direction, lenght)  # линия хода
        
        if set(move_line) != {None}:  # если линия хода не пустая
            if (set(move_line[:-1]) != None and
                    move_line[-1].get_color() == piece.get_color()):
                # и если на последней клетки хода не стоит противник, фигура того же цвета
                return False
        

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

