f = 0
d = 0
n = int(input())
for i in range(n):
    a = input()
    if ('Кот' in a or 'кот' in a) and ('Пёс' not in a and 'пёс' not in a):
        d += 1
        if f == 1:
            f = 0
    elif 'Пёс' in a or 'пёс' in a:
        f = 1:
if d >= 1 and f == 0:
    print('МЯУ')
else:
    print('НЕТ')