count = 0
first = set()
second = set()
n = int(input())
for i in range(n):
    s = input()
    if s in first:
        first.remove(s)
        count += 2
    elif s in second:
        count += 1
    else:
        first.add(s)
        second.add(s)
print(count)
