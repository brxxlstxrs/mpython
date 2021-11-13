a = set()
b = set()
m = int(input())
n = int(input())
for i in range(m):
    a.add(input())
for i in range(n):
    b.add(input())
d = len(a ^ b)
if m - n or d:
    print(d)
else:
    print('NO')
