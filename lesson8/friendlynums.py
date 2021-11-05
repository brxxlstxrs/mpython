for i in range(0, 10000):
    n1 = 0
    n2 = 0
    for x in range(1, i):
        if i % x == 0:
            n1 += x
    for z in range(1, n1):
        if n1 % z == 0:
            n2 += z
    if i == n2 and i != n1 and i == min(i, n1):
        print(i, n1)
