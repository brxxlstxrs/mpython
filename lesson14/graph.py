lst = []
rec = map(int, input().split())
for i in rec:
    tmp = []
    for j in range(1, max(rec) + 1):
        if j < i:
            tmp.append(' ')
        else:
            tmp.append('*')
    lst.append(tmp)
print(lst)
