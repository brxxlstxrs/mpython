def password_level(password: str):
    if len(password) < 6:
        a = 'Недопустимый пароль'
    elif password.isdigit() or password.islower() or password.isupper():
        a = 'Ненадежный пароль'
    elif password.isalnum() or password.isalpha():
        a = 'Слабый пароль'
    else:
        a = 'Надежный пароль'
    return a

