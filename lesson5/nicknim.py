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
        print('ИИ выйграл!')
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
                    print('Вы выйграли!')