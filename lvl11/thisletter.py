class LenError(Exception):
    pass


class NegativeIndex(Exception):
    pass


s = input()
i = int(input())
letter = input()
try:
    if i < 1:
        raise NegativeIndex
    if len(letter) > 1:
        raise LenError
    if letter in s:
        if s[i - 1] == letter:
            print('ДА')
        else:
            print('НЕТ')
except (IndexError, LenError, NegativeIndex):
    print('ОШИБКА')
