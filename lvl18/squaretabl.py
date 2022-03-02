def squared(a, b, k):
    tencnt = 10
    for i in range(a, b + 1):
        if i * i % k != 0:
            print(f'{i * i:<4}', end = '')
        if i == a + tencnt - 1:
                print()
                tencnt += 10
 
