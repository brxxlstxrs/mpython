count = 0
n = int(input())
while n > 1:
    if n % 2:
        n -= 1
    else:
        n /= 2
    count += 1
print(count)