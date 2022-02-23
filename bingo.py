from random import sample
# from pprint import pprint


def make_bingo():
    lst = sample(range(1, 76), 24)
    lst.insert(12, 0)
    return tuple(tuple(lst[i:i + 5]) for i in range(0, 21, 5))


# pprint(make_bingo())
