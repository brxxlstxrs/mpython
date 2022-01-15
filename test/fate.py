import statistics
res = []
lst = []
line = input()
while line != '':
    lst.append([int(i) for i in line.split('*')])
    line = input()
for i in zip(*lst):
    mid = statistics.mean(i)
    l = [j for j in i if j > mid]
    if l:
        res.append(min(l))
    else:
        print('NO DIGITS')
        break
print(*sorted(set(res))[::-1])
