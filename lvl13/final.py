dct = {}
lst = []
for i in range(int(input())):
    dct[int(input())] = input()
for i in sorted(dct.keys())[len(dct) // 2::-1]:
    lst.append(i)
    print(lst)
