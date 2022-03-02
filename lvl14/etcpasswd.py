import re
lst = []
while (s := input()) != '':
    lst.append(s)
passwds = input().split(';')
for i in range(len(lst)):
    lst[i] = re.split(r':|, ', lst[i])
for i in lst:
    if i[1] in passwds:
        print(f'To: {i[0]}\n{i[4]}, ваш пароль слишком простой, смените его.')
