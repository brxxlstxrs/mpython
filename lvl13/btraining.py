first = []
second = []
count = 0
dct = {1: first, 2: second}
for i in range(int(input())):
    n = int(input())
    first.append(n)
    second.append(n)
for i in range(int(input())):
    dct[int(input())][int(input())] += int(input())
for i in range(len(first)):
    if first[i] == second[i]:
        count += 1
print(*first)
print(*second)
print(count)

