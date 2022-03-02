c = set()
n = int(input())
for i in range(n):
    c.add(input())
w = input()
if w in c:
    print('TRY ANOTHER')
else:
    print('OK')
