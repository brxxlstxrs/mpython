num, k = 0, 1
for i in range(int(input())):
    a, b = int(input()), int(input())
    num = num * b + a * k
    k *= b
    x, y = num, k
    while y > 0:
        x, y = y, x % y
print(num // x, '/', k // x)