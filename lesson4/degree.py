d = 0
n = int(input())
if n == 1:
    print(0)
while n > 1:
    n = n / 2
    d += 1
    if n == 1:
        print(d)
    elif n < 1:
        print('НЕТ')