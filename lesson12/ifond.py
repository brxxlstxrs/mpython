lst = [int(input()) for i in range(int(input()))]
print(*lst, sep='\n', end='\n\n')
print(*tuple(i * 3 for i in lst), sep='\n')
