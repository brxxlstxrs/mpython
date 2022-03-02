s1 = input()
s2 = input()
if s1[-1] == 'ь':
    s1 = s1[:-1]
if s2[0] == s1[-1]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
