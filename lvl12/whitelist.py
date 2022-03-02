l1 = tuple(input() for i in range(int(input())))
l2 = tuple(input() for i in range(int(input())))
print(*[i for i in l2 for j in l1 if i ==j], sep='\n')
