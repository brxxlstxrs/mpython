y, x = map(range, (int(input()), int(input())))
tabl = [[input() for _ in x] for _ in y]
res = []
# print(*tabl, sep='\n')
if len(tabl) > 1:
    res.append(' '.join(tabl.pop(0)))
end = ' '.join(tabl.pop())
for i in tabl:
    res.append(' '.join(sorted(i, key=len, reverse=True)))
res.append(end)
print(*res, sep='\n')
