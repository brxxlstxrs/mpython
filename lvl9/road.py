a = set()
b = set()
while (n := input()) != '':
    n = int(n)
    a.add(n)
while (n := input()) != '':
    n = int(n)
    b.add(n)
c = a & b
if c:
    print(*c, sep='\n')
else:
    print('EMPTY')
