# Урок 4 - Знакомство с циклом while

# Вспомнить всё: if
s = float(input())
if s < 15.5:
    print('ХОЛОДНО')
elif s > 28:
    print('ЖАРКО')
else:
    print('НОРМАЛЬНО')

# password123
if len(password := input()) >= 8:
    if (password1 := input()) == password:
        print('OK')
    else:
        print('Различаются.')
else:
    print('Короткий!')

# Числа до нуля
while (n := int(input())) != 0:
    print(n)

# Строки до пустой
while (n := input()) != '':
    print(n)

# Учитель
n = int(input())
while n % 8 != n:
    n = n // 8
print(n)

# Скидки
count = 0
while (price := float(input())) > 0:
	if price > 1000:
		price *= 0.95
	count += price
print(count)

# Таких берут в космонавты
count = 0
high = 0
low = 192
while (n := input()) != '!':
	n = int(n)
	if n > 149 and n < 191:
		count += 1
		if n > high:
			high = n
		if n < low:
			low = n
print(count)
print(low, high)

# Сколько строк?
c = 1
while (s := input()) != 'Спасибо.':
    c += 1
print(c)

# Среднее
sm = 0
c = 0
while (t := float(input())) > -301:
	c += 1
	sm += t
print(sm / c)

# 1024 и все-все-все
d = 0
n = int(input())
if n == 1:
    print(0)
while n > 1:
    n = n / 2
    d += 1
    if n == 1:
        print(d)
    elif n < 1:
        print('НЕТ')

# password123456
if len(password := input()) > 7 and '123' not in password:
    if (password1 := input()) == password:
        print('OK')
    else:
        print('Различаются.')
elif len(password) < 8:
    print('Короткий!')
else:
    print('Простой!')

# Круглые
while (a := int(input())) % 10 == 0:
    print(a)

# password
k = ''
while k != 'OK':
    password = input()
    password1 = input()
    if len(password) > 7 and '123' not in password:
        if password1 == password:
            k = 'OK'
            print(k)
        else:
            print('Различаются.')
    elif len(password) < 8:
        print('Короткий!')
    else:
        print('Простой!')

# Лабиринт с правом на ошибку
#flag = True
#while flag:
#    floor = input('Тут пахнет сыростью, ты не'
#                  ' помнишь как тут оказался.'
#                  '\nПеред тобой развилка, куда пойдешь '
#                  '(направо, налево, прямо) ')
#    if floor == 'направо' or floor == 'налево':
#        print('Ты немного прошелся', floor, 'и нашел',
#              'старые ступени\nобнесеные пылью.')
#        while flag:
#            nfloor = input('Хочешь спуститься вниз? (да/нет) ')
#            if nfloor == 'нет':
#                print('Ты стоял, не зная что делать и ждал чего-то,')
#                print('вдруг с потолка мндленно начала слазить',
#                      'огромная паучиха,')
#                print('когда она подобралась к тебе,',
#                      'начала обвивать тебя паутиной.')
#                print('Дальше ты ничего не помнишь')
#                flag = False
#            elif nfloor == 'да':
#                while flag:
#                    floor = input('Тут опять пахнет сыростью.'
#                                  'Ты как-будто видешь ее.'
#                                  '\nТебе хочется обернуться (да/нет) ')
#                    if floor == 'да':
#                        print('Ты видешь как в тебя летит стрела,',
#                              'но уже поздно')
#                        print('все как будто сжимается вокруг,',
#                              'ты ничего не чуствуешь.')
#                        print('Похоже это самая глупая концовка')
#                        flag = False
#                    elif floor == 'нет':
#                        print('Ты идешь вперед земля идет под уклон')
#                        print('ты решил пойти еще дальше...')
#                        print('Ты нашел сокровищницу с кучей',
#                              'драгоценностей')
#                        flag = False
#                    else:
#                        print('ошибочный ввод')
#                        continue
#            else:
#                print('ошибочный ввод')
#                continue
#    elif floor == 'прямо':
#        print('ты пошел прямо, оступился и упал с большой высоты...')
#        flag = False
#    else:
#        print('ошибочный ввод')
#        continue

# Сиракузская последовательность
step = 0
n = int(input())
while n > 1:
    if n % 2:
        n = 3 * n + 1
    else:
        n /= 2
    step += 1
print(step)

# Бинарная угадайка v2.0
approve = ''
upperb = 1001
lowb = 1
print(500)
while True:
    approve = input()
    if approve == '<':
        upperb = (lowb + upperb) // 2
    elif approve == '>':
        lowb = (lowb + upperb) // 2
    else:
        break
    print((lowb + upperb) // 2)

# Ищем клад — 1
# x - где находится клад по координате x
# y - где находится клад по координате y
x = int(input())
y = int(input())
x1 = 0  # x1 - где мы находимся по x
y1 = 0  # y1 - где мы находимся по y
count = 0
direction = 2
'''direction - направление:
     → == 1, ↑ == 2, ← == 3, ↓ == 4'''
while not (x1 == x and y1 == y):
    command = input()  # спрашиваем действие
    count += 1
    if command == 'налево':  # определяем настоящее направление 
        direction += 1
    elif command == 'направо':
        direction -= 1
    elif command == 'разворот':
        direction += 2
    else:
        n = int(input())
        if direction == 2:
            y1 += n
        elif direction == 4:
            y1 -= n
        elif direction == 1:
            x1 += n
        else:
            x1 -= n
    '''если направление 5 то мы повернулись на 360 
    следовательно направление 1 и т.д'''
    if direction > 4:
        direction -= 4
    elif direction < 1:
        direction += 4
#    print('направление', direction)
#    print('x -', x1, 'y -', y1)
print(count)
if direction == 1:
    print('восток')
elif direction == 2:
    print('север')
elif direction == 3:
    print('запад')
else:
    print('юг')


