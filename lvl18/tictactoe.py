def tic_tac_toe(field: list):
    field1 = [set(i) for i in field]
    field1.extend([set(i) for i in zip(*field)])
    d = [[field[i][i] for i in range(len(field))]]
    d.append([field[i][len(field)-i-1] for i in range(len(field))])
    field1.extend([set(i) for i in d])
    print(*field1)
    if {'x'} in field1:
        print('x win')
    elif {'0'} in field1:
        print('0 win')
    else:
        print('draw')


data = """0 - 0
x x x
0 0 -"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
