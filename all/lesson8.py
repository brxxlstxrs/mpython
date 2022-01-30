# Урок 8 - Вложенные циклы

# Таблица умножения
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j * i, end='\t')
    print()

# Таблица не в виде таблицы
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, '*', j, '=', j * i)

# Ёлочный счёт
n = int(input())
c = 1
cc = 0
for i in range(1, n + 1):
    print(i, end=' ')
    cc += 1
    if cc == c:
        c += 1
        cc = 0
        print()

# Логистический максимин
count = 0
flag1 = 1
flag2 = 1
a = 0
b = 0
bglobal = 0
n1 = 0
n = int(input())
for i in range(n):
    n1 = int(input())
    for j in range(n1):
        a = int(input())
        if flag1:
            b = a
            flag1 = 0
        if a < b:
            b = a
    flag1 = 1
    if flag2:
        bglobal = b
        flag2 = 0
    if bglobal <= b:
        bglobal = b
        count = i + 1
print(count, bglobal)

# Таблица деления
n = int(input())
n1 = int(input())
for j in range(1, n1 + 1):
    for i in range(1, n + 1):
        print(i / j, end=' ')
    print('\n', end='')

# Рисуем прямоугольник
height = int(input())
width = int(input())
s = input()
print(s * width)
for i in range(height - 2):
    print(s, ' ' * (width - 2), s, sep='')
print(s * width)

# Дальние командировки
n = int(input())
tmp = 9
i = 1
k = 0
while i * tmp < n:
    n -= tmp * i
    i += 1
    tmp = 10 * tmp
if i - 1:
    k = int('9' * (i - 1))
f = n // i + k
print(f)

# Обратный отсчёт: серия пусков
n = int(input())
i = 0
for j in range(n):
    for i in range(j, -1, -1):
        print('Осталось секунд:', i)
    print('Пуск', j + 1)

# Простые числа на миллион долларов
flag = 0
n = int(input())
if n == 3:
    print(2)
else:
    if n > 3:
        print(2, 3, sep='\n')
    for i in range(1, n, 2):
        for j in range(2, int(i / 2) + 1):
            if i % j != 0:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            print(i)
    
# Начинающий фермер
credit = int(input())
livestock = int(input())
for b in range(1, min(livestock, credit // 20) + 1):
    for k in range(0, min(livestock, credit // 10) + 1):
        for t in range(0, min(livestock, credit // 5) + 1):
            if b * 20 + k * 10 + t * 5 == credit:
                if b + k + t == livestock:
                    print(b, k, t)

# Числовая дружба
for i in range(0, 10000):
    n1 = 0
    n2 = 0
    for x in range(1, i):
        if i % x == 0:
            n1 += x
    for z in range(1, n1):
        if n1 % z == 0:
            n2 += z
    if i == n2 and i != n1 and i == min(i, n1):
        print(i, n1)

# Пифагоровы тройки
n = int(input())
m = int(n ** (1 / 2)) + 1
p = ''
for i in range(1, m + (m + 1) % 2, 2):
    for j in range(2, m + m % 2, 2):
        if i * i + j * j < n + 1:
            a = 2 * i * j
            b = abs(i * i - j * j)
            c = i * i + j * j
            a1, bb = a, b
            while a1 != bb:
                if a1 > bb:
                    a1 = a1 - bb
                else:
                    bb = bb - a1
            bb = c
            while a1 != bb:
                if a1 > bb:
                    a1 = a1 - bb
                else:
                    bb = bb - a1
            d = a1
            d2 = str(min(a // d, b // d)) + ' ' + str(max(a // d, b // d))
            d2 += ' ' + str(c // d) + ' '
            if d2 not in p:
                print(d2)
            p += d2
