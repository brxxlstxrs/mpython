for _ in range(int(input())):
    f = 0
    lst = list(map(int, input().split()))
    slst = list()
    csh = 100
    while lst:
        if lst[0] == csh:
            csh = lst.pop(0)
        elif lst[-1] == csh:
            csh = lst.pop()
        elif lst[0] < csh:
            csh = lst.pop(0)
        elif lst[-1] < csh:
            csh = lst.pop()
        else:
            f = 1
            break
        slst.append(csh)
    if f:
        print('НЕТ')
        continue
    print(*slst)
