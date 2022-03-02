from itertools import permutations
ss = list('ABCDEFGH')


def get_coords(s):
    return ss.index(s[0]) + 1, int(s[1])


def get_str(x, y):
    return ''.join((ss[x - 1], str(y)))


def possible_turns(cell):
    cell = list(cell)
    x, y = get_coords(cell)
    res = set()
    for i, j in permutations(range(-2, 3), 2):
        if i != 0 and j != 0 and abs(j) != abs(i):
                if 0 < x + i < 9 and 0 < y + j < 9:
                    res.add(get_str(x + i, y + j))
    return sorted(res)
