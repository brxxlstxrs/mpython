key = 1
s = ''
gb = 'пока'
g2 = 'прощай'
g3 = 'досвидания'
print('Привет я программа говорилка')
while key:
    words = input()
    lw = words.lower()
    if (gb in lw or
            g2 in lw or g3 in lw):
        print('Ну ладно пока(я пыталась поговорить с тобой)')
        key = 0
    if 'прив' in lw:
        print('Ещё раз привет')
    if 'здравству' in lw:
        print('Тебе тоже здоровья')
    if 'как' in lw and ('ты' in lw or 'дела' in lw):
        print('Мне отлично живется')
    if len(words) == 1 and words.isupper():
        s = input('Напиши что-то')
        print('а Я ВОТ ТАК МОГУ', s.swapcase())
    if 'нет' in lw:
        print('Ну нет и нет')
    if 'да' in lw:
        print('Да, хорошо')
    if 'интерес' in lw:
        print('введи несколько строк(остановка - когда увижу знак q)')
        while 'q' not in s:
            s += input()
        print(s)
    if 'глуп' in lw or 'ум' in lw:
        print('Да так....')
        print('Я еще совсем неопытная программа')
        print('Зато умею вот так:')
        print('.\n'*1000)