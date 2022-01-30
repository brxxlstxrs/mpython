# Урок 3 - Простые встроенные функции

# Каникулы капризного ребёнка
a = input()
b = input()
if a != b and \
        (a == 'Тула' and b != 'Пенза' or b == 'Пенза' and a != 'Тула'):
    print('ДА')
else:
    print('НЕТ')

# Факториал: первое знакомство
print(2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)

# Полтора землекопа
if (1400 % (2 * 3)) == 0:
    print(1400 // (2 * 3))
else:
    print(1400 // (2 * 3) + 1)

# Количество минут в году
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
minutes_per_year = minutes_per_hour * hours_per_day * days_per_year
print(minutes_per_year)

# Сложить два числа
a = int(input())
b = int(input())
print(a + b)

# Сложить ещё два числа
a = float(input())
b = float(input())
print(a + b)

# Одно число
n = float(input())
if abs(n) <= 1e-6:
    print(1000000)
else:
    print(n**-1)

# Длина
w = input()
print('Слово', w, 'имеет длину', len(w))

# На раз-два-три, рассчитайсь!
a = int(input())
b = int(input())
c = int(input())
if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a
print(a)
print(b)
print(c)

# Плюс-минус
n = float(input())
if n > 0:
    print('+')
elif n < 0:
    print('-')
else:
    print(0)

# Високосность
y = int(input())
if y % 4 == 0 and y % 100 != 0:
    print('Високосный')
elif y % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')

# Калькулятор
n1 = float(input())
n2 = float(input())
sg = input()
if sg == '+':
    print(n1 + n2)
elif sg == '-':
    print(n1 - n2)
elif sg == '*':
    print(n1 * n2)
elif sg == '/':
    if n2 != 0:
        print(n1 / n2)
    else:
        print(888888)
else:
    print(888888)

# Уравнение
a = 999999
b = 142857
x = a - b
print(x)

# Пополам
n = int(input())
if n % 2 == 0:
    print('чётное')
else:
    print('нечётное')

# Верстаем визитную карточку
s = input()
print((len(s) * 2) + 3)

# Собери число
h = int(input())
n = ((h // 10) % 10)
n1 = (h // 100) + n
n2 = (h % 10) + n
if n1 > n2:
    print(str(n1) + str(n2))
else:
    print(str(n2) + str(n1))

# Красивое число
n = int(input())
a = n // 100
b = ((n // 10) % 10)
c = n % 10
if a <= b and a <= c:
    if b >= c:
        if (a + b) / 2 == c:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
    elif c >= b:
        if (a + c) / 2 == b:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
elif b <= a and b <= c:
    if a >= c:
        if (b + a) / 2 == c:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
    elif c >= a:
        if (b + c) / 2 == a:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
elif c <= a and c <= b:
    if a >= b:
        if (c + a) / 2 == b:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
    elif b >= a:
        if (c + b) / 2 == a:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')

# Четырехзначный минимум
n = int(input())
a = n % 10
b = n % 100 // 10
c = n // 100 % 10
d = n // 1000
if a > b:
    a, b = b, a 
if b > c:
    b, c = c, b 
if c > d:
    c, d = d, c 
if a > b:
    a, b = b, a 
if b > c:
    b, c = c, b 
if a > b:
    a, b = b, a 
if a == 0 and b:
    a, b = b, a 
elif a == 0 and b == 0 and c:
    a, c = c, a
elif a == 0 and b == 0 and c == 0:
    a, d = d, a
print(int(str(a) + str(b) + str(c) + str(d)))
