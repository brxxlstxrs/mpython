dct = {}
for i in range(int(input())):
    v, k = input().split()[::2]
    if k in dct:
        dct[k].append(v)
    else:
        dct[k] = [v]
for i in range(int(input())):
    s = input()
    if s in dct:
        print(*dct[s])
    else:
        print()
    
