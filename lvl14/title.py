lst = []
for _ in range(int(input())):
    elems = ''
    while (s := input()) != '*':
        elems += ' ' + s
    elems = '-'.join(elems.strip().split())
    lst.append(elems)
print(*lst[::-1], sep=', ')
