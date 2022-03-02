n = int(input())
n1 = int(input())
for j in range(1, n1 + 1):
    for i in range(1, n + 1):
        print(i / j, end=' ')
    print('\n', end='')
