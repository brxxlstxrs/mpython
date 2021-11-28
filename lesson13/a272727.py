c = 0
lst = [0]
for j in range(int(input()) - 1):
    for i in range(len(lst)):
        if lst[i] == lst[-i - 1]:
            c += 1
    lst.append(c)
    c = 0
print(*lst, sep='\n')

