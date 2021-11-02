n = int(input())
c = 1
cc = 0
for i in range(1, n + 1):
    print(i, end=' ')
    cc += 1
    if cc == c:
        c += 1
        cc = 0
        print('\n', end='')
