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