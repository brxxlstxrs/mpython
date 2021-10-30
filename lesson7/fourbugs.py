count = 0
side = float(input())
sp = float(input())
while side - sp >= 0.01:
    side = ((side - sp) ** 2 + sp ** 2) ** 0.5
    count += 1
print(count)