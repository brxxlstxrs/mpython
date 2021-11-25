s = []
tpl = tuple(input() for i in range(int(input())))
srch = tuple(input() for i in range(int(input())))
for j in tpl:
    if all([i in j for i in srch]):
        s.append(j)
print(*s, sep='\n')
