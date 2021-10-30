cat = False
s = ''
n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s.lower():
        cat = True
    if 'пёс' in s.lower():
        cat = False
print('МЯУ' * cat or 'НЕТ')