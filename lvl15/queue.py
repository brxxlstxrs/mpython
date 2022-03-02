lst = []
for _ in range(int(input())):
    s = input()[:-1].split(' - ')
    if s[0][:3] == 'Кто':
        lst.append(s[-1])
    elif s[0][:1] == 'Я':
        lst.insert(0, s[-1])
    else:
        if lst:
            print(f'Заходит {lst.pop(0)}!')
        else:
            print('В очереди никого нет.')
