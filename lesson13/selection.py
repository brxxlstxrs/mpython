tpl = tuple(input() for i in range(int(input())))
print(*[i for i in tpl], sep='\n', end='\n\n')
print(*[i for i in tpl if '5' in i or '4' in i], sep='\n')
