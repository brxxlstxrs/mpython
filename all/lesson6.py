# Урок 6 - Знакомство с циклом for

# Делите ли
count = 0
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        count += 1
        print(i, end=' ')
print()     
if a == 1:
    print('НЕТ')
elif count > 2:
    print('НЕТ')
else:
    print('ПРОСТОЕ')

# Ждём потепления
count = 0
while (t := float(input())) < 22.0:
    count += 1
print(count // 7)

# Повторение - мать учения: ultimate edition
st = input()
n = int(input())
for i in range(n):
    print(st)

# Кубизм
n = int(input())
for i in range(n + 1):
    print('Куб числа', i, 'равен', i ** 3)

# Факториал
n = int(input())
f = 1
for i in range(2, n + 1):
    f *= i
print(f)

# Перемножить без трюков
comp = 1
for i in range(6):
    if (n := int(input())) != 0:
        comp *= n
print(comp)

# Вышел зайчик погулять
s = []
n = int(input())
for i in range(n + 1):
    s.append(str(i))
print(' '.join(s))

# Обратный отсчёт
print(*map("Осталось секунд: {}".format, range(int(input()), -1, -1)), "Пуск", sep="\n")

# Пирамида
n = int(input())
for i in range(n):
    print((' ' * (n - i - 1)) + ('*' * (i * 2 + 1)))

# Тест на делимость
d = 0
for i in range(17):
    d = int(input())
    if i % d == 0:
        print('ДА')
    else:
        print('НЕТ')

# Умнее среднего
n = int(input())
amount = 0
iq = 0
for i in range(n):
    iq = int(input())
    if i == 0:
        print(0)
    elif iq > amount / i:
        print('>')
    elif iq < amount / i:
        print('<')
    else:
        print(0)
    amount += iq

# Шварценеггер против Годзиллы
num, k = 0, 1
for i in range(int(input())):
    a, b = int(input()), int(input())
    num = num * b + a * k
    k *= b
    x, y = num, k
    while y > 0:
        x, y = y, x % y
print(num // x, '/', k // x, sep='')

# Дзета-функция Римана
pi = 3.14159265358979323846264338327950288419716939937510
amount = 0
n = int(input())
for i in range(1, n + 1):
    amount += 1 / (i ** 2)
print((pi ** 2) / amount)

# Сумма ряда
param = -1
summ = 0
n = int(input())
for i in range(n):
    summ += int(input()) * (param := -param)
print(summ)

# Конфетное изобилие
count = int(input())
nmax = int((2 * count) ** (1 / 2))
for i in range(nmax, 0, -1):
    if (2 * count - i * i + i) % (2 * i) == 0:
        print((2 * count - i * i + i) // (2 * i))
        break
