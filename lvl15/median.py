data = list(map(int, input().split()))
if len(data) % 2 == 0:
    d = data[len(data) // 2 - 1], data[len(data) // 2]
    d = sum(d) / 2
else:
    d = float(data[len(data) // 2])
print(sum(data) / len(data), d)
