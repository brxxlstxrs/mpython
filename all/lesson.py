# Урок 1 - Знакомство со средой

# Приветствие
print('Привет, Яндекс!')

# Знакомство
print('Привет, Яндекс!\nПриятно познакомиться.')

# Эхо-1
s = 'Ауууу!'
print(s)
print(s)

# Эхо-1.1
s = 'Ауууууу!'
print(s)
print(s)

# Взлом «планетной» угадайки
print(planet)  # type: ignore

# Попугай
a = str(input())
b = '\n' + str(input())
c = '\n' + str(input())
print(a, b, c)

# Билетная касса
a = input()
b = input()
c = input()
print('Билет на \"', a, '\" в \"', b, '\" на', str(c), 'забронирован.')

# Обратный попугай
a = input()
b = input()
c = input()
print(c)
print(b)
print(a)

# Бит или не бит?
bite = str(8 * 1024)
print('1 бит - минимальная единица количества информации.')
print('1 байт = 8 бит.')
print('1 Килобит = 1024 бита.')
print('1 Килобайт = 1024 байта.')
print('1 Килобайт =', bite, 'бит.')

# Гороскоп
name = input()
surname = input()
favorite_animal = input()
zodiac_sign = input()
print('Индивидуальный гороскоп для пользователя', name, surname)
print('Кем вы были в прошлой жизни:', favorite_animal)
print('Ваш знак зодиака -', zodiac_sign, ', поэтому вы - тонко чувствующая натура.')

# Отчет о приветствии
print('Моя первая программа напечатала "Привет, Яндекс!" :)')

# Эхо-1.2
s = 'Ауууу!'
print('Человек:', s)
print('Эхо:', s)

# Взлом планетной угадайки — 2
warning = planet  # type: ignore

# Взлом планетной угадайки — 3
answer = planet  # type: ignore


