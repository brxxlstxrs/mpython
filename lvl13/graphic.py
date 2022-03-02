lst = []
lst2 = []
s = ''
n1 = int(input())
input()
for _ in range(n1):
    lst.append(list(input()))
for i in range(n1):
    if i % 2 == 0:
        for j in range(len(lst[i])):
            if j % 2 == 0:
                s += lst[i][j]
        lst2.append(s)
        s = ''
print(*lst2, sep='\n')
