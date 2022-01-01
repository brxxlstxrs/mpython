lst = []
n = int(input())
field = [tuple(input()) for _ in range(n)]
for i in range(n - 2):
    for j in range(n - 2):
        lst.extend((
            tuple(set(field[i][j:j + 3])),
            tuple(set(field[i + 1][j:j + 3])),
            tuple(set(field[i + 2][j:j + 3])),
            tuple(set((
                field[i][j],
                field[i + 1][j],
                field[i + 2][j],
                ))),
            tuple(set((
                field[i][j + 1],
                field[i + 1][j + 1],
                field[i + 2][j + 1],
                ))),
            tuple(set((
                field[i][j + 2],
                field[i + 1][j + 2],
                field[i + 2][j + 2],
                ))),
            tuple(set((
                field[i][j],
                field[i + 1][j + 1],
                field[i + 2][j + 2]
                ))),
            tuple(set((
                field[i][j + 2],
                field[i + 1][j + 1],
                field[i + 2][j]
                )))
            ))
st = set(lst)
if ('o',) in st:
    print('o')
elif ('x',) in st:
    print('x')
else:
    print('-')
