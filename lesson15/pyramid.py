for _ in range(int(input())):
    f = 0
    lst = list(map(int, input().split()))
    slst = list()
    csh = 100
    while lst:
        match lst[0], lst[-1], csh:
            case 
        slst.append(csh)
    if f:
        print('НЕТ')
        continue
    print(*slst)
