# Урок 7 -True и False, break и continue

# FizzBuzz
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# Найди кота
flag = 0
s = ''
n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s.lower():
        flag = 1
if flag:
    print('МЯУ')
else:
    print('НЕТ')

# Найди кота — 2
l= 0
line = 1
while (str := input()) != 'СТОП':
    if 'кот' not in str.lower():
        line += 1
    else:
        l = line
        break
if l > 0:
    print(l)
else:
    print(-1)

# Найди кота (break)
n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s.lower():
        print('МЯУ')
        break
else:
    print('НЕТ')

# Найди кота — 2 (break)
count = 1
while (n := input()) != 'СТОП':
    if 'кот' in n or 'Кот' in n:
        print(count)
        break
    else:
        count += 1
else:
    print(-1)

# Сложиться до 10
summ = 0
count = 0
while (n := int(input())) != 0:
    count += 1
    summ += n
    if summ == 10:
        print(count)
        break

# 1984
n = int(input())
evrasia = True
ostasia = False
for i in range(n):
    q = input()
    if q == 'С кем война?':
        print('Евразия' * evrasia or 'Остазия' * ostasia)
    elif q == 'С кем мир?':
        print('Евразия' * ostasia or 'Остазия' * evrasia)
    else:
        evrasia, ostasia = ostasia, evrasia

# Найди кота — 3
lines = 0
l = -1
count = 1
while (s := input()) != 'СТОП':
    if 'кот' in s.lower() and l == -1:
        l = count
        lines += 1
    elif 'кот' in s.lower():
        lines += 1
    count += 1
print(lines, l)

# Ищем клад — 2
x1 = 0
y1 = 0
count = 0
flag = 0
x = int(input())
y = int(input())
while (s := input()) != 'стоп':
    if not(x1 == x and y1 == y) and flag == 0:
        count += 1
    else:
        flag = 1
    n = int(input())
    if s == 'север':
        y1 += n
    elif s == 'юг':
        y1 -= n
    elif s == 'запад':
        x1 -= n
    elif s == 'восток':
        x1 += n
print(count)

# Найди кота — 4
cat = False
s = ''
n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s.lower():
        cat = True
    if 'пёс' in s.lower():
        cat = False
print('МЯУ' * cat or 'НЕТ')

# Школа танцев
count = 1
rcount = 0
wrong = 0
s = ''
r = {1: 'раз', 2: 'два', 3: 'три', 4: 'четыре'}
cwrong = int(input())
while wrong != cwrong:
    s = input()
    if s != r[count]:
        print('Правильных отсчётов было ', rcount, ', но теперь вы ошиблись.', sep='')
        wrong += 1
        count = 1
        rcount = 0
    else:
        rcount += 1
        count += 1
        if count > 4:
            count = 1
print('На сегодня хватит.')

# Многоразовый калькулятор
c = ''
f = 1
while c != 'x':
    a = int(input())
    c = input()
    if c == 'x':
        print(a)
        break
    else:
        if c == '+':
            b = int(input())
            print(a + b)
        elif c == '!' and a > 0:
            for i in range(1, a + 1):
                f *= i
            print(f)
        elif a == 0 and c == '!':
            print('1')
        elif c == '*':
            b = int(input())
            print(a * b)
        elif c == '-':
            b = int(input())
            print(a - b)
        elif c == '/':
            b = int(input())
            if b == 0:
                continue
            else:
                print(a // b)
        elif c == '%':
            b = int(input())
            if b == 0:
                continue
            else:
                print(a % b)

# Биржевой робот
n = 1
ln = 0
lb = False
ll = False
buy = 0
sale = 0
c = 0
while n != 0:
    ln = n
    n = int(input())
    c += 1
    if ln < n and not lb and c > 1 and not ll:
        buy = n
        lb = True
    elif ln > n and lb and not ll:
        sale = n
        ll = True
print(buy, sale, (sale - buy))


# Проверка блокчейна
# ???

# Заводные жуки в квадрате
count = 0
side = float(input())
sp = float(input())
while side - sp >= 0.01:
    side = ((side - sp) ** 2 + sp ** 2) ** 0.5
    count += 1
print(count)
