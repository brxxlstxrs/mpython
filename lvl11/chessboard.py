a = list(map(chr, range(65, 74)))[: int(input())]
n = len(a)
for i in range(n, 0, -1):
    for j in a:
        print(j + str(i), end=' ')
    print()
