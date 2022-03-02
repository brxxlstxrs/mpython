n = 0
tpl = tuple(int(input()) for i in range(int(input())))
s, e = int(input()), int(input())
for i in range(s - 1, e):
    n += tpl[i]
print(n)
