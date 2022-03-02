class LessError(Exception):
    pass
s = input()
i = int(input())
try:
    if i < 1:
        raise LessError
    print(s[i - 1])
except (IndexError, LessError):
    print('ОШИБКА')
