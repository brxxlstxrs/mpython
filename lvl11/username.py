from string import ascii_lowercase, digits
c = ascii_lowercase + digits + '_'
s = input()
for i in s:
    if i not in c:
        print('Неверный символ:', i)
        break
else:
    print('OK')
