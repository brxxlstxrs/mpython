import sys
from random import choice

lst = [i.strip() for i in sys.stdin]
lst1 = lst[:]
data = set()
for i in lst:
    while True:
        y = lst1[:]
        y.remove(i) if i in y else 0
        pair = i, choice(y)
        if pair not in data:
            data.update((pair, pair[::-1]))
            lst1.remove(pair[1]) if pair[1] in lst1 else 0
            break
    print(f'{pair[0]} - {pair[1]}')
