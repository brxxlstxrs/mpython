# Урок 5 - Отладчик

# Банк
print('Добро пожаловать в интернет-банк!')
print('У нас фантастические процентные ставки!')
print('Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,')
print('для вкладов на сумму до 100 тысяч включительно - 20%,')
print('для более 100 тысяч - 30%!')
print('На какую сумму желаете сделать вклад?')
money = float(input())
if money <= 10000:
    money *= 1.1
elif money <= 100000:
    money *= 1.2
elif money > 100000:
    money *= 1.3
print('Вы получаете', money, '₽, поздравляем!')

# Фибоначчи
n = int(input())
a, b = 1, 1
while a <= n:
    print(a)
    a, b = b, a + b

# Ним-пасьянс
qty = int(input())
while qty > 0:
    step = int(input())
    print(qty := qty - step)

# Псевдоним-пасьянс
qty = int(input())
while qty:
    step = int(input())
    if (step < 4) and (step > 0) and (step <= qty):
        qty -= step
    print(qty)

# Псевдоним v2.0
key = 1
bunch = int(input())
while bunch:
    key = 1
    step = bunch % 4
    if step == 0:
        step = 2
    bunch -= step
    print(step, bunch)
    if bunch == 0:
        print('ИИ выиграл!')
    else:
        while key:
            step = int(input())
            if step > 3:
                print('Некорректный ход:', step)
            elif step < 1:
                print('Некорректный ход:', step)
            elif step > bunch:

                print('Некорректный ход:', step)
            else:
                bunch -= step
                key = 0
                print(step, bunch)
                if bunch == 0:
                    print('Вы выиграли!')

# Остров невезения
d = int(input())
m = int(input()) - 2
y = int(input())
if m < 1:
    m = m + 12
    y = y - 1
c = y // 100
y = y % 100
luck = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(luck)

# Цирк, цирк, цирк!
count = 0
n = int(input())
while n > 1:
    if n % 2:
        n -= 1
    else:
        n /= 2
    count += 1
print(count)

# Псевдоним-мизер
key = 1
bunch = int(input())
while bunch:
    key = 1
    step = (bunch - 1) % 4
    if step == 0:
        step = 2
    bunch -= step
    print(step, bunch)
    if bunch == 0:
        print('Вы выиграли!')
    else:
        while key:
            step = int(input())
            if step > 3:
                print('Некорректный ход:', step)
            elif step < 1:
                print('Некорректный ход:', step)
            elif step > bunch:
                print('Некорректный ход:', step)
            else:
                bunch -= step
                key = 0
                print(step, bunch)
                if bunch == 0:
                    print('ИИ выиграл!')

# Лабиринт 2
#err = 'ошибка'
#do = ''
#color = ''
#acolor = ''
#n = 4
#c4 = 'синюю'
#c3 = 'красную'
#c2 = 'фиолетовую'
#c1 = 'оранжевую'
#print('Ты оказался под землей')
#print('Ты ничего не помнишь но сверку капает так,')
#print('как будто над тобой находится канализация города')
#print('Продвигаться куда либо тяжело, ты находишься по колено в мутной воде')
#while 1:
#    if n == 4:
#        color = c4
#    elif n == 3:
#        color = c3
#    elif n == 2:
#        color = c2
#    else:
#        color = c1
#    print('Ты видешь перед собой решетку хочешь сломать её?(да/нет)')
#    do = input('перед тем как ответить подумай\n')
#    print('Молодец')
#    if do == 'да':
#        print('Ты сломал решетку и вода затопила соседнюю полость')
#        print('Ты слышишь чьи то голоса')
#        print('Три огромных черепахи идут в твою сторону')
#        print('они что-то говорят про плохую пиццу')
#        print('они смотрят в твою сторону и заставляют сьесть тебя пиццу')
#        if 'оранж' not in acolor:
#            print('ты отравляешься пиццей')
#            print('GAME OVEEEEEER')
#            break
#        else:
#            print('Это были черепашки ниндзя')
#            print('Они признают тебя за Микеланджело из-за оранжевой тряпки')
#            print('которую они увидели у тебя')
#            print('Ты выйграл, но...')
#            break
#    elif do == 'нет':
#        print('Но странно, что ты теперь хочешь сделать(искать другой выход/подождать)')
#        do = input()
#        if do == 'подождать':
#            continue
#        elif do == 'искать другой выход':
#            print('Ты начал искать другой выход...')
#            do = input('Тебе не надоело?(да/нет/другое)\n')
#            if do == 'да' or do == 'нет':
#                print('Тебе походу прийдется сломать решетку')
#                continue
#            else:
#                print('Ты все таки продолжаешь поиски')
#                print('Ты нашел', color, 'тряпку')
#                acolor = color
#                n -= 1
#                do = input('Продолжить поиски?(да/нет)\n')
#                if do == 'да':
#                    print('Ты нашел скрытую лестницу наверх')
#                    print('когда ты лез ты упал с нее и она как-то исчезла')
#                    print('Ты перевязываешь тряпкой рану и снова забываешься')
#                    if acolor == 'оранжевую':
#                        acolor = 'фиолетовую'
#                    continue
#                elif do == 'нет':
#                    print('Ты повязываешь тряпку на голову')
#                    continue
#                else:
#                    print(err)
#                    break
#        else:
#            print(err)
#            break
#    else:
#        print(err)
#        break
#print('Ты вдруг просыпаешься')

# Бот-говорилка
#key = 1
#s = ''
#gb = 'пока'
#g2 = 'прощай'
#g3 = 'досвидания'
#print('Привет я программа говорилка')
#while key:
#    words = input()
#    lw = words.lower()
#    if (gb in lw or
#            g2 in lw or g3 in lw):
#        print('Ну ладно пока(я пыталась поговорить с тобой)')
#        key = 0
#    elif 'прив' in lw:
#        print('Ещё раз привет')
#    elif 'здравству' in lw:
#        print('Тебе тоже здоровья')
#    elif 'как' in lw and ('ты' in lw or 'дела' in lw):
#        print('Мне отлично живется')
#    elif len(words) == 1 and words.isupper():
#        s = input('Напиши что-то')
#        print('а Я ВОТ ТАК МОГУ', s.swapcase())
#    elif 'нет' in lw:
#        print('Ну нет и нет')
#    elif 'да' in lw:
#        print('Да, хорошо')
#    elif 'интерес' in lw:
#        print('введи несколько строк(остановка - когда увижу знак q)')
#        while 'q' not in s:
#            s += input()
#        print(s)
#    elif 'глуп' in lw or 'ум' in lw:
#        print('Да так....')
#        print('Я еще совсем неопытная программа')
#        print('Зато умею вот так:')
#        print('.\n' * 1000)
#    else:
#        print('У меня нет кода чтобы ответить тебе')

# Ним2-пасьянс
n1 = int(input())
n2 = int(input())
while (n1 != 0) or (n2 != 0):
    num = int(input())
    if num == 1:
        k = int(input())
        n1 -= k
        print(n1, n2)
    elif num == 2:
        f = int(input())
        n2 -= f
        print(n1, n2)

# Ним3-пасьянс
lst = [int(input()) for i in range(3)]
while lst.count(0) != len(lst):
    ind = int(input()) - 1
    lst[ind] -= int(input())
    print(*lst)

# Ним-2 v2.0
pile = [int(input()) for i in range(2)]
while True:
    # AI section
    if pile[0] > pile[1]:
        base = pile[0] - pile[1]
        pile[0] -= base
        base = 1, base
    elif pile[1] > pile[0]:
        base = pile[1] - pile[0]
        pile[1] -= base
        base = 2, base
    else:
        pile[0] -= 1
        base = 1, 1
    print(*base, *pile)
    if set(pile) == {0}:
        print('ИИ выиграл!')
        break

    # Human section
    while True:
        p = int(input())  # numper of pile
        n = int(input())  # number of deducted
        if 0 < p < 3 and 0 < n <= pile[p - 1]:
            break
        print('Некорректный ход:', p, n)
    # calculate human turn
    pile[p - 1] -= n
    print(p, n, *pile)
    if set(pile) == {0}:
        print('Вы выиграли!')
        break

# Ним-3 v2.0
pil = [int(input()) for i in range(3)]
while True:
    # AI section
    nim = pil[0] ^ pil[1] ^ pil[2]  # calculating nim-sum
    if nim == 0:  # if nim-sum = 0
        mv = [pil.index(max(pil)), 1]
    else:
        for i in range(3):
            # winning move
            if 0 <= pil[i] ^ nim < pil[i]:
                mv = [i, pil[i] - (pil[i] ^ nim)]
                break
    pil[mv[0]] -= mv[1]  # type: ignore
    mv[0] += 1           # type: ignore
    print(*mv, *pil)
    if set(pil) == {0}:
        print('ИИ выиграл!')
        break
    # Human section
    while True:
        p = int(input())
        n = int(input())
        if 0 < p < 4 and 0 < n <= pil[p - 1]:
            break
        print('Некорректный ход:', p, n)
    pil[p - 1] -= n
    print(p, n, *pil)
    if set(pil) == {0}:
        print('Вы выиграли!')
        break
