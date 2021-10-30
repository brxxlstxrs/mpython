count = 1
rcount = 0
wrong = 0
s = ''
r = {1 : 'раз', 2 : 'два', 3 : 'три', 4 : 'четыре'}
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