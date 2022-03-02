last = set()
now = set()
n = int(input())
for i in range(n):
    m = int(input())
    for j in range(m):
        now.add(input())
    if i == 0:
        last = now
    last = last & now
    now.clear()
print(*last, sep='\n') 
