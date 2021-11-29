import operator as opr


def share(s: str):
    try:
        a, o, b = s.strip().split(' ')
        return a, b, o
    except ValueError:
        return


def calc(ia: str, ib: str, o: str):
    op_dct = {
        '*': opr.mul,
        '+': opr.add,
        '-': opr.sub,
        '/': opr.truediv
    }
    if ia.isdigit() and ib.isdigit():
        a, b = map(int, (ia, ib))
    else:
        print('Error')
        return
    match ord(o):
        case 42 | 43 | 45 | 47:
            pass
        case _:
            print('Error')
            return
    print(a, o, b, '=', op_dct[o](a, b))
    return


if __name__ == '__main__':
    while (s := input()) != 'q':
        try:
            calc(*share(s))
        except TypeError:
            print('Error')
