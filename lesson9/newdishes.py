can = set()
already = set()
for i in range(int(input())):
    can.add(input())
for i in range(int(input())):
    for j in range(int(input())):
        already.add(input())
print(can - already)
